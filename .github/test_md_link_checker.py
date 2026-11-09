"""Offline regression tests: python -m unittest discover -s .github -p 'test_*.py'."""

import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import md_link_checker as checker


class MediaExtractionTests(unittest.TestCase):
    def urls(self, text: str) -> list[str]:
        return [url for _, url in checker.extract_links_from_md(text)]

    def test_markdown_images_with_empty_alt_and_titles(self):
        self.assertEqual(
            checker.extract_links_from_md(
                "![](https://example.org/empty.png) "
                '![Map](https://example.org/map.png "Map title")'
            ),
            [
                ("<image>", "https://example.org/empty.png"),
                ("Map", "https://example.org/map.png"),
            ],
        )

    def test_local_image_with_spaces_and_parentheses(self):
        self.assertEqual(
            self.urls("![Map](<assets/my map.png>) ![](assets/map(1).png)"),
            ["assets/my map.png", "assets/map(1).png"],
        )

    def test_html_media_attributes_are_not_bare_urls(self):
        self.assertEqual(
            self.urls(
                '<IMG alt="Map"\n SRC="https://example.org/map.png?x=1&amp;y=2" />'
                "<video src='https://example.org/movie.mp4' poster='poster.jpg'>"
                '<source src=https://example.org/movie.webm type="video/webm">'
                '</video><iframe src="https://example.org/embed/1"></iframe>'
            ),
            [
                "https://example.org/map.png?x=1&y=2",
                "https://example.org/movie.mp4",
                "poster.jpg",
                "https://example.org/movie.webm",
                "https://example.org/embed/1",
            ],
        )

    def test_escaped_and_nested_parentheses(self):
        self.assertEqual(
            self.urls(r"![Map](assets/map\(1\).png) ![](assets/a(b(c)).png)"),
            ["assets/map(1).png", "assets/a(b(c)).png"],
        )

    def test_html_anchor_links_are_preserved(self):
        self.assertEqual(
            self.urls("<a href=https://example.org/page>Site</a>"),
            ["https://example.org/page"],
        )

    def test_uppercase_http_scheme_in_media(self):
        self.assertEqual(
            self.urls('<img src="HTTPS://example.org/map.png">'),
            ["https://example.org/map.png"],
        )

    def test_first_reference_definition_wins(self):
        self.assertEqual(
            self.urls(
                "![Map][id]\n[id]: https://example.org/first.png\n"
                "[ID]: https://example.org/second.png"
            ),
            ["https://example.org/first.png"],
        )

    def test_reference_images(self):
        self.assertEqual(
            self.urls(
                "![Map][Satellite view] ![Logo][] ![Shortcut]\n"
                '[satellite   VIEW]: <assets/map.png> "Map"\n'
                "[logo]: assets/logo.svg\n[shortcut]: assets/shortcut.gif\n"
            ),
            ["assets/map.png", "assets/logo.svg", "assets/shortcut.gif"],
        )

    def test_remote_reference_image_is_not_checked_twice(self):
        self.assertEqual(
            self.urls('![Map][map]\n[map]: https://example.org/map.png "Map"'),
            ["https://example.org/map.png"],
        )

    def test_linked_image_checks_both_targets(self):
        self.assertEqual(
            self.urls(
                "[![Video](https://example.org/thumb.jpg)](https://example.org/watch)"
            ),
            ["https://example.org/thumb.jpg", "https://example.org/watch"],
        )

    def test_protocol_relative_media(self):
        self.assertEqual(
            self.urls('<img src="//example.org/map.jpg">'),
            ["https://example.org/map.jpg"],
        )

    def test_media_in_code_and_comments_is_ignored(self):
        self.assertEqual(
            self.urls(
                '```html\n<img src="https://example.org/code.png">\n```\n'
                "`![](https://example.org/inline.png)`\n"
                "<!-- ![](https://example.org/comment.png) -->"
            ),
            [],
        )

    def test_embedded_and_unsupported_schemes_are_ignored(self):
        self.assertEqual(
            self.urls(
                '<img src="data:image/png;base64,abc"><video src="blob:abc">'
                "![](file:///outside.png) ![](#fragment) ![](javascript:alert(1))"
            ),
            [],
        )

    def test_duplicate_media_is_deduplicated(self):
        self.assertEqual(self.urls("![](map.png) ![](map.png)"), ["map.png"])

    def test_existing_link_forms_still_work(self):
        self.assertEqual(
            self.urls(
                "[Site](https://example.org/page) <https://example.org/angle> "
                "https://example.org/bare."
            ),
            [
                "https://example.org/page",
                "https://example.org/angle",
                "https://example.org/bare",
            ],
        )


class MediaCheckingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(
            prefix="media-check-test-", dir=checker.REPO_ROOT
        )
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.patch_root = patch.object(checker, "REPO_ROOT", self.root)
        self.patch_root.start()
        self.addCleanup(self.patch_root.stop)
        (self.root / "stories").mkdir()
        (self.root / "assets").mkdir()
        (self.root / "assets" / "map image.png").write_bytes(b"image")
        self.story = self.root / "stories" / "story.md"
        self.story.write_text(
            "![](../assets/map%20image.png?version=1#preview)\n"
            '<video src="/assets/missing.mp4"></video>',
            encoding="utf-8",
        )

    def test_collectors_resolve_local_media_consistently(self):
        expected = [
            ("stories/story.md", "<image>", "assets/map%20image.png"),
            ("stories/story.md", "<video>", "assets/missing.mp4"),
        ]
        self.assertCountEqual(checker.collect(self.root), expected)
        self.assertCountEqual(checker.collect_from_files([self.story]), expected)

    def test_escaped_image_path_checks_existing_file(self):
        (self.root / "assets" / "map(1).png").write_bytes(b"image")
        self.story.write_text(r"![](../assets/map\(1\).png)", encoding="utf-8")
        tasks = checker.collect_from_files([self.story])
        self.assertEqual(len(tasks), 1)
        self.assertEqual(checker.check_url(tasks[0])[3], 200)

    def test_duplicate_reference_checks_first_missing_target(self):
        self.story.write_text(
            "![Map][id]\n[id]: ../assets/missing.png\n"
            "[id]: ../assets/map%20image.png",
            encoding="utf-8",
        )
        tasks = checker.collect_from_files([self.story])
        self.assertEqual(len(tasks), 1)
        self.assertEqual(checker.check_url(tasks[0])[3], 404)

    def test_invalid_local_path_does_not_abort_audit(self):
        self.assertEqual(
            checker.check_url(("story.md", "<image>", "assets/%00.png"))[3], 404
        )

    def test_local_presence_checks_do_not_make_http_requests(self):
        with patch.object(checker, "_do_request") as request:
            statuses = [
                checker.check_url(task)[3] for task in checker.collect(self.root)
            ]
        self.assertCountEqual(statuses, [200, 404])
        request.assert_not_called()

    def test_directories_and_paths_outside_repository_are_missing(self):
        for url in ("assets", "../outside.png"):
            with self.subTest(url=url):
                self.assertEqual(
                    checker.check_url(("story.md", "<image>", url))[3], 404
                )

    def test_local_history_keys_are_distinct_and_preserve_case(self):
        self.assertEqual(
            checker.normalize("assets/map%20image.png"), "local:assets/map image.png"
        )
        self.assertNotEqual(
            checker.normalize("assets/Map.png"), checker.normalize("assets/map.png")
        )
        self.assertNotEqual(
            checker.normalize("assets/a.png"), checker.normalize("assets/b.png")
        )

    def test_remote_media_preserves_query_and_closes_response(self):
        response = Mock(
            status_code=206, url="https://example.org/movie.mp4?token=example"
        )
        with patch.object(checker, "_do_request", return_value=response) as request:
            result = checker.check_url(("story.md", "<video>", response.url))
        self.assertEqual(result, ("story.md", "<video>", response.url, 200))
        request.assert_called_once_with(response.url, checker.UAS[0], use_cffi=False)
        response.close.assert_called_once_with()

    def test_missing_remote_media_is_broken(self):
        response = Mock(status_code=404, url="https://example.org/missing.png")
        with patch.object(checker, "_do_request", return_value=response):
            self.assertEqual(
                checker.check_url(("story.md", "<image>", response.url))[3], 404
            )
        response.close.assert_called_once_with()

    def test_both_http_clients_stream_media(self):
        for use_cffi, target in (
            (False, checker.requests),
            (True, checker.cffi_requests),
        ):
            with self.subTest(use_cffi=use_cffi), patch.object(target, "get") as get:
                checker._do_request(
                    "https://example.org/movie.mp4", checker.UAS[0], use_cffi=use_cffi
                )
                self.assertTrue(get.call_args.kwargs["stream"])
                self.assertEqual(get.call_args.kwargs["headers"]["Range"], "bytes=0-0")

    def test_pr_mode_fails_for_new_missing_media_and_writes_report(self):
        report = self.root / "report.html"
        with (
            patch.object(checker, "OUTPUT_HTML", report),
            patch.object(checker, "load_previous_report", return_value=None),
            patch.dict(checker.os.environ, {"FULL_AUDIT": ""}),
            patch("sys.argv", ["md_link_checker.py", "--files", str(self.story)]),
            contextlib.redirect_stdout(io.StringIO()),
            self.assertRaises(SystemExit) as error,
        ):
            checker.main()
        self.assertEqual(error.exception.code, 1)
        self.assertIn("assets/missing.mp4 [404]", report.read_text(encoding="utf-8"))

    def test_pr_mode_accepts_known_missing_media(self):
        baseline = {"broken_links": ["local:assets/missing.mp4"], "ok_links": []}
        with (
            patch.object(checker, "OUTPUT_HTML", self.root / "report.html"),
            patch.object(checker, "load_previous_report", return_value=baseline),
            patch.dict(checker.os.environ, {"FULL_AUDIT": ""}),
            patch("sys.argv", ["md_link_checker.py", "--files", str(self.story)]),
            contextlib.redirect_stdout(io.StringIO()),
        ):
            checker.main()

    def test_full_audit_records_missing_and_present_media(self):
        history = self.root / "health_history"
        with (
            patch.object(checker, "OUTPUT_HTML", self.root / "report.html"),
            patch.object(checker, "HISTORY_DIR", history),
            patch.dict(checker.os.environ, {"FULL_AUDIT": "1"}),
            patch("sys.argv", ["md_link_checker.py"]),
            contextlib.redirect_stdout(io.StringIO()),
        ):
            checker.main()
        payload = json.loads(next(history.glob("*.json")).read_text(encoding="utf-8"))
        self.assertEqual(payload["total_checked"], 2)
        self.assertEqual(payload["broken_links"], ["local:assets/missing.mp4"])
        self.assertEqual(payload["ok_links"], ["local:assets/map image.png"])


if __name__ == "__main__":
    unittest.main()
