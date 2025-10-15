import os
import re
import json
import sys
import yaml
import requests
from io import BytesIO
from PIL import Image
from urllib.parse import urlparse, unquote

# Get base URL from command-line argument or set a default
BASE_URL = (
    sys.argv[1]
    if len(sys.argv) > 1
    else "https://esa-eodashboards.github.io/RACE-narratives/"
)


def url_to_safe_filename(url, suffix="_preview.png"):
    parsed_url = urlparse(url)
    # Extract and decode the base file name from the path
    filename = os.path.basename(parsed_url.path)
    filename = unquote(filename)  # Decode URL-encoded parts

    # Remove query parameters if accidentally included in filename
    filename = filename.split("?")[0].split("#")[0]

    # Remove extension and append your custom suffix
    name_root = os.path.splitext(filename)[0]

    # Replace unsafe characters with underscores
    safe_name = re.sub(r"[^A-Za-z0-9._-]", "_", name_root)

    # Add suffix
    return safe_name + suffix


def fetch_and_resize_image(image_url, output_dir, target_width):
    try:
        # Extract filename from URL
        image_name = url_to_safe_filename(image_url)
        if not image_name:  # Fallback if URL ends with '/'
            image_name = "image_preview.png"

        # Download image from URL
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))

        # Resize while preserving aspect ratio
        w_percent = target_width / float(img.size[0])
        h_size = int(float(img.size[1]) * w_percent)
        img = img.resize((target_width, h_size), Image.LANCZOS)

        # Save to output directory
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, image_name)
        img.save(output_path)

        relpath = os.path.join("assets/previews", image_name)
        return os.path.relpath(relpath, start=".").replace("\\", "/")

    except Exception as e:
        print(f"[warn] Couldn't load/resize image from URL {image_url}: {e}")
        return None


def extract_metadata(file_path, base_url):
    """Extracts frontmatter metadata, first H1, first H3, and image URL from a Markdown file."""
    metadata = {}
    img_url = ""
    filename = os.path.basename(file_path)
    file_url = base_url.rstrip("/") + "/" + filename  # Ensure proper URL format

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Extract frontmatter metadata (YAML-like block at the start)
    frontmatter_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if frontmatter_match:
        frontmatter_text = frontmatter_match.group(1)
        try:
            metadata = yaml.safe_load(frontmatter_text)  # Convert to dictionary
        except yaml.YAMLError:
            print(f"Warning: Could not parse frontmatter in {file_path}")

    # Extract first H1 header
    h1_match = re.search(r"# (.+?)\s*<!--{.*?}-->", content)
    if h1_match and not metadata.get("title"):
        metadata.update({"title": h1_match.group(1)})

    # Extract first H3 header
    h3_match = re.search(r"### (.+?)\s*<!--{.*?}-->", content)
    if h3_match and not metadata.get("subtitle"):
        metadata.update({"subtitle": h3_match.group(1)})

    # Extract first image URL
    img_match = re.search(r'<!--{.*?src="(.*?)".*?}-->', content)
    if img_match:
        img_url = fetch_and_resize_image(
            img_match.group(1), "output/assets/previews", 300
        )
        metadata.update({"image": img_url})

    # Change official to provider, so that we do not have to update all stories
    if metadata.get("official"):
        metadata.update({"provider": "agency"})
    else:
        metadata.update({"provider": "community"})

    metadata.update({"file": file_url})
    return metadata


# Create output directory
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Process all Markdown files
metadata_list = []
for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".md") and file != "README.md" and "scripts" not in root:
            file_path = os.path.join(root, file)
            metadata = extract_metadata(file_path, BASE_URL)
            if any(metadata.values()):
                metadata_list.append(metadata)


# Save JSON metadata
with open(
    os.path.join(output_dir, "narratives.json"), "w", encoding="utf-8"
) as json_file:
    json.dump(metadata_list, json_file, indent=2, ensure_ascii=False, default=str)
