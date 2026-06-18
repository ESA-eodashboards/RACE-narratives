#!/usr/bin/env python3
import os
import sys
import re
import json
import argparse
import requests
import html
import urllib3
import random
import time
from datetime import datetime, timezone
from urllib.parse import urlparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)

# -------------------------------------------------------------------
# Config
# -------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
OUTPUT_HTML = SCRIPT_DIR / "link_check_report.html"

# Files skipped by the script
EXCLUDED_FILES = {"readme.md"}

# History
HISTORY_DIR = Path(os.environ.get("HISTORY_DIR", REPO_ROOT / "health_history"))
HISTORY_PREFIX = "health_report_"

TIMEOUT = 10
MAX_WORKERS = 20

RUN_URL = os.environ.get("GITHUB_RUN_URL", "")


# -------------------------------------------------------------------
# Normalize URL
# -------------------------------------------------------------------
def normalize(url: str) -> str:
    if not url:
        return ""
    url = html.unescape(url.strip())
    if not url.startswith("http"):
        return ""
    p = urlparse(url)
    netloc = p.netloc.lower().replace("www.", "")
    path = p.path.rstrip("/")
    return f"{netloc}{path}"


# -------------------------------------------------------------------
# Check URL
# -------------------------------------------------------------------
def check_url(task):
    file_key, name, url = task
    last_status = "ERR"
    last_final = url
    # Try plain requests with two UAs, then curl_cffi (TLS-fingerprint
    # impersonation). Stop early on a non-bot-block status.
    attempts = [(False, UAS[0]), (False, UAS[1]), (True, UAS[0])]
    for i, (use_cffi, ua) in enumerate(attempts):
        try:
            r = _do_request(url, ua, use_cffi=use_cffi)
            last_final = str(r.url)
            # Range request → 206 Partial Content means the URL is fine.
            status = 200 if r.status_code == 206 else r.status_code
            last_status = status
            if status not in (403, 405, 429, 503):
                return file_key, name, last_final, status
        except Exception:
            last_status = "ERR"
        if i < len(attempts) - 1:
            time.sleep(0.3 + random.random() * 0.4)
    return file_key, name, last_final, last_status


# -------------------------------------------------------------------
# Browser-like request helpers (bypass naive bot detection)
# -------------------------------------------------------------------
UAS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
]


def browser_headers(url: str, ua: str) -> dict:
    parsed = urlparse(url)
    return {
        "User-Agent": ua,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
        "image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "Referer": f"{parsed.scheme}://{parsed.netloc}/",
        "DNT": "1",
        # Range avoids HEAD blocks and skips downloading the full body
        "Range": "bytes=0-0",
    }


def _do_request(url, ua, use_cffi=False):
    headers = browser_headers(url, ua)
    if use_cffi:
        return cffi_requests.get(
            url,
            headers=headers,
            allow_redirects=True,
            timeout=TIMEOUT,
            verify=False,
            impersonate="chrome124",
        )
    s = requests.Session()
    return s.get(
        url,
        headers=headers,
        allow_redirects=True,
        timeout=TIMEOUT,
        verify=False,
    )


# -------------------------------------------------------------------
# Extract links from a Markdown file
# -------------------------------------------------------------------
# [text](url) — captures both label and URL
MD_LINK_RE = re.compile(r'\[([^\]]+)\]\(\s*(https?://[^\s)]+)\s*(?:"[^"]*")?\)')
# <https://...>
ANGLE_URL_RE = re.compile(r"<(https?://[^>\s]+)>")
# Bare URLs
BARE_URL_RE = re.compile(r'(?<![\("<\[])\b(https?://[^\s<>\)\]]+)')


def extract_links_from_md(text):
    """
    Returns list of (label, url). label = link text for [text](url),
    or "<bare>" for unlabeled URLs.
    Strips trailing punctuation from bare URLs.
    """
    results = []
    seen = set()

    # Remove fenced code blocks so we don't check sample URLs there.
    text_wo_code = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text_wo_code = re.sub(r"`[^`]*`", "", text_wo_code)

    for m in MD_LINK_RE.finditer(text_wo_code):
        label = m.group(1).strip()
        url = m.group(2).strip().rstrip(".,;:!?")
        key = (label, url)
        if key not in seen:
            seen.add(key)
            results.append((label, url))

    for m in ANGLE_URL_RE.finditer(text_wo_code):
        url = m.group(1).strip().rstrip(".,;:!?")
        key = ("<bare>", url)
        if key not in seen:
            seen.add(key)
            results.append(("<bare>", url))

    # Mask already-matched [text](url) so BARE_URL_RE won't re-pick them
    masked = MD_LINK_RE.sub("", text_wo_code)
    masked = ANGLE_URL_RE.sub("", masked)
    for m in BARE_URL_RE.finditer(masked):
        url = m.group(1).strip().rstrip(".,;:!?)")
        key = ("<bare>", url)
        if key not in seen:
            seen.add(key)
            results.append(("<bare>", url))

    return results


# -------------------------------------------------------------------
# HTML writer
# -------------------------------------------------------------------
def write_html(groups, prev_broken=None):
    prev_broken = prev_broken or set()
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write("""
<html>
<head>
<meta charset="UTF-8">
<title>Link Checker Report</title>
<style>
body { font-family: Arial, sans-serif; line-height: 1.5; padding: 20px; }
.file { font-weight: bold; font-size: 1.2em; margin-top: 25px;
        border-bottom: 1px solid #ddd; padding-bottom: 5px; }
.entry { margin-left: 15px; padding: 2px 0; }
.green  { color: green; }
.red    { color: red; }
.gold   { color: goldenrod; }
.purple { color: purple; font-weight: bold; }
</style>
</head>
<body>
<h2>Link Checker Report</h2>
<p>
Purple = newly broken link<br>
Red = already known broken link
</p>
""")
        for file, entries in groups.items():
            f.write(f'<div class="file">{html.escape(file)}</div>\n')
            for name, url, status in entries:
                normalized = normalize(url)
                known_broken = status != 200 and normalized in prev_broken
                newly_broken = status != 200 and normalized not in prev_broken

                if status == 200:
                    color, tag = "green", ""
                elif newly_broken:
                    color, tag = "purple", " ⚠️ NEW"
                elif known_broken:
                    color, tag = "red", ""
                elif status in (301, 302, 307, 308, 403, 405):
                    color, tag = "gold", ""
                else:
                    color, tag = "red", ""

                text = f"{name}: {url} [{status}]{tag}"
                f.write(f'<div class="entry {color}">{html.escape(text)}</div>\n')
        f.write("</body></html>")


# -------------------------------------------------------------------
# Collect tasks (full audit) — every .md file in the repo
# -------------------------------------------------------------------
SKIP_DIRS = {".git", "node_modules", "health_history", ".github"}


def collect(repo_root: Path):
    tasks = []
    for root, dirs, files in os.walk(repo_root):
        # prune
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for file in files:
            if not file.lower().endswith(".md"):
                continue
            fp = Path(root) / file
            if file.lower() in EXCLUDED_FILES:
                print(f"ℹ️ Skipping excluded file: {fp}")
                continue
            try:
                with open(fp, "r", encoding="utf-8") as f:
                    text = f.read()
            except Exception:
                continue
            rel = fp.relative_to(repo_root).as_posix()
            for name, url in extract_links_from_md(text):
                tasks.append((rel, name, url))
    return tasks


def collect_from_files(file_paths):
    tasks = []
    for fp in file_paths:
        p = Path(fp)
        if p.name.lower() in EXCLUDED_FILES:
            print(f"ℹ️ Skipping excluded file: {fp}")
            continue
        if not p.exists() or not p.is_file():
            print(f"⚠️ Skipping missing file: {fp}")
            continue
        if p.suffix.lower() != ".md":
            continue
        try:
            with open(p, "r", encoding="utf-8") as f:
                text = f.read()
        except Exception as e:
            print(f"⚠️ Could not read {fp}: {e}")
            continue
        try:
            rel = p.resolve().relative_to(REPO_ROOT).as_posix()
        except ValueError:
            rel = p.as_posix()
        for name, url in extract_links_from_md(text):
            tasks.append((rel, name, url))
    return tasks


# -------------------------------------------------------------------
# History helpers
# -------------------------------------------------------------------
def load_previous_report():
    if not HISTORY_DIR.exists():
        return None
    files = sorted(HISTORY_DIR.glob(f"{HISTORY_PREFIX}*.json"))
    if not files:
        return None
    try:
        with open(files[-1], "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️ Could not read previous report: {e}")
        return None


def write_new_report(total_checked, broken_links, ok_links):
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H-%M-%S_UTC")
    path = HISTORY_DIR / f"{HISTORY_PREFIX}{ts}.json"
    payload = {
        "timestamp_utc": ts,
        "total_checked": total_checked,
        "errors": len(broken_links),
        "html_report_workflow_run": RUN_URL,
        "html_report_note": (
            "Download the colour-coded HTML report "
            "from the workflow artifacts on the page above."
        ),
        "broken_links": sorted(broken_links),
        "ok_links": sorted(ok_links),
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    print(f"📝 Wrote {path}")
    return path


# -------------------------------------------------------------------
# Main
# -------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Markdown link checker")
    parser.add_argument(
        "--files",
        nargs="*",
        default=None,
        help="Specific Markdown files to check (PR mode)",
    )
    args = parser.parse_args()

    full_audit_env = os.environ.get("FULL_AUDIT", "").strip() == "1"
    is_pr_mode = args.files is not None and not full_audit_env

    print("\n🚀 Running Markdown link checker")
    print(f"📂 Repo root:   {REPO_ROOT}")
    print(f"📂 History dir: {HISTORY_DIR}")

    prev = load_previous_report()
    prev_ok = set(prev.get("ok_links", [])) if prev else set()
    prev_broken = set(prev.get("broken_links", [])) if prev else set()

    # ---------------------------------------------------------------
    # PR MODE
    # ---------------------------------------------------------------
    if is_pr_mode:
        print(f"📄 PR mode — checking {len(args.files)} changed file(s)")
        tasks = collect_from_files(args.files)
        print(f"\n🔗 Total links in changed files: {len(tasks)}")

        if not prev:
            print("ℹ️ No previous baseline found.")

        groups = {}
        regressions = []
        new_broken = []

        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
            futures = [ex.submit(check_url, t) for t in tasks]
            for future in as_completed(futures):
                file, name, url, status = future.result()
                groups.setdefault(file, []).append((name, url, status))
                normalized = normalize(url)
                if status != 200:
                    if normalized in prev_ok:
                        regressions.append((file, name, url, status))
                        print(f"❌ REGRESSION: {status} {url}")
                    elif normalized not in prev_broken:
                        new_broken.append((file, name, url, status))
                        print(f"⚠️ NEW BROKEN LINK: {status} {url}")

        write_html(groups, prev_broken)

        print("\n--- PR check summary ---")
        print(f"Regressions:      {len(regressions)}")
        print(f"New broken links: {len(new_broken)}")
        if regressions or new_broken:
            raise SystemExit(1)
        print("✅ OK: no regressions.")
        return

    # ---------------------------------------------------------------
    # FULL AUDIT MODE
    # ---------------------------------------------------------------
    print("📂 Full audit mode — scanning every .md file in the repo")
    tasks = collect(REPO_ROOT)
    print(f"\n🔗 Total links: {len(tasks)}")

    if not tasks:
        print("✅ Nothing to check.")
        write_html({})
        return

    groups = {}
    broken_links = set()
    ok_links = set()

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = [ex.submit(check_url, t) for t in tasks]
        for future in as_completed(futures):
            file, name, url, status = future.result()
            groups.setdefault(file, []).append((name, url, status))
            normalized = normalize(url)
            if status == 200:
                ok_links.add(normalized)
            else:
                broken_links.add(normalized)

    write_html(groups, prev_broken)
    write_new_report(
        total_checked=len(tasks),
        broken_links=broken_links,
        ok_links=ok_links,
    )

    curr_errors = len(broken_links)
    newly_broken = broken_links - prev_broken
    fixed = prev_broken - broken_links

    print("\n--- Health trend ---")
    print(f"Previous errors: {prev.get('errors') if prev else 'n/a'}")
    print(f"Current errors:  {curr_errors}")
    print(f"Fixed links:     {len(fixed)}")
    print(f"Newly broken:    {len(newly_broken)}")

    if newly_broken:
        print("\n--- Newly broken links ---")
        for u in sorted(newly_broken):
            print(f"  • {u}")

    print("\n✅ Full audit complete.")

    prev_errors = prev.get("errors") if prev else None
    if isinstance(prev_errors, int) and curr_errors > prev_errors:
        print(
            f"\n❌ Failing: current broken links ({curr_errors}) "
            f"exceed previous ({prev_errors})."
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
