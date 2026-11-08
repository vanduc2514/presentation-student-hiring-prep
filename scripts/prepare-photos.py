#!/usr/bin/env python3
"""Prepare the photographic images used on the deck's media cards.

Each photo is downloaded from its documented source, centre-cropped to the
media card's aspect ratio, and given the deck's warm muted grade so photos sit
in the same palette as the paper cards and the charts.

All sources are CC0 1.0 (public domain dedication), so no attribution is
legally required. Credits are recorded anyway in slides/images/photos/CREDITS.md.

    python3 scripts/prepare-photos.py
"""

import urllib.request
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "slides" / "images" / "photos"

SIZE = (900, 1100)
TARGET_RATIO = SIZE[0] / SIZE[1]
QUALITY = 86

# Warm muted grade: near-monochrome with a paper-coloured cast, so photos read
# as part of the same print-like system as the charts.
SATURATION = 0.35
CONTRAST = 1.06
WARM = (1.03, 1.00, 0.95)

PHOTOS = [
    {
        "file": "laptop-alone.jpg",
        "url": "https://images.rawpixel.com/editor_1024/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcHgxMzk3NzE2LWltYWdlLWt3dnkwOW8wLmpwZw.jpg",
        "title": "Woman working laptop",
        "creator": "Rawpixel",
        "license": "CC0 1.0",
        "page": "https://www.rawpixel.com/image/5924243/photo-image-public-domain-hand-technology",
        "used_for": "Slide 2 - the question every candidate is asking",
    },
    {
        "file": "whiteboard-explain.jpg",
        "url": "https://cdn.stocksnap.io/img-thumbs/960w/DVGAHMPSXF.jpg",
        "title": "Whiteboard Meeting",
        "creator": "Kristin Hardwick",
        "license": "CC0 1.0",
        "page": "https://stocksnap.io/photo/whiteboard-meeting-DVGAHMPSXF",
        "used_for": "Slide 7 - explaining a decision out loud",
    },
    {
        "file": "paper-stacks.jpg",
        "url": "https://images.rawpixel.com/editor_1024/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIyLTA1L3B4NTM2MjEyLWltYWdlLWt3dnhua241LmpwZw.jpg",
        "title": "Free stacks paper files image",
        "creator": "Rawpixel",
        "license": "CC0 1.0",
        "page": "https://www.rawpixel.com/image/5922472/photo-image-paper-texture-public-domain",
        "used_for": "Slide 10 - ranking, not rejecting",
    },
    {
        "file": "scorecard-form.jpg",
        "url": "https://cdn.stocksnap.io/img-thumbs/960w/TBJ9OPDGMK.jpg",
        "title": "Checklist Goals",
        "creator": "Glenn Carstens-Peter",
        "license": "CC0 1.0",
        "page": "https://stocksnap.io/photo/checklist-goals-TBJ9OPDGMK",
        "used_for": "Slide 11 - the eight boxes the panel fills in",
    },
    {
        "file": "code-screen.jpg",
        "url": "https://live.staticflickr.com/677/32294675551_0d02e99735_b.jpg",
        "title": "code-screen-monitor",
        "creator": "CCØBAY",
        "license": "CC0 1.0",
        "page": "https://www.flickr.com/photos/151198978@N08/32294675551",
        "used_for": "Slide 19 - the evidence stack",
    },
]


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "slide-deck/1.0"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return Image.open(BytesIO(response.read())).convert("RGB")


def crop_to_ratio(image, ratio):
    width, height = image.size
    if width / height > ratio:
        new_width = int(height * ratio)
        left = (width - new_width) // 2
        return image.crop((left, 0, left + new_width, height))
    new_height = int(width / ratio)
    top = (height - new_height) // 2
    return image.crop((0, top, width, top + new_height))


def grade(image):
    image = ImageEnhance.Color(image).enhance(SATURATION)
    image = ImageEnhance.Contrast(image).enhance(CONTRAST)
    red, green, blue = image.split()
    red = red.point(lambda v: min(255, int(v * WARM[0])))
    green = green.point(lambda v: min(255, int(v * WARM[1])))
    blue = blue.point(lambda v: min(255, int(v * WARM[2])))
    return Image.merge("RGB", (red, green, blue))


def credits(entries):
    lines = [
        "# Photo credits",
        "",
        "All photographs are **CC0 1.0** (public domain dedication): free to use",
        "commercially, no attribution required. Sources are recorded here so the",
        "provenance of every image in the deck is traceable.",
        "",
        "Regenerate the processed files with `python3 scripts/prepare-photos.py`.",
        "",
        "| File | Title | Creator | Licence | Source | Used on |",
        "|---|---|---|---|---|---|",
    ]
    for entry in entries:
        lines.append(
            f"| `{entry['file']}` | {entry['title']} | {entry['creator']} | "
            f"{entry['license']} | [{entry['page'].split('//')[1][:46]}...]({entry['page']}) | "
            f"{entry['used_for']} |"
        )
    lines.append("")
    return "\n".join(lines)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for entry in PHOTOS:
        image = fetch(entry["url"])
        image = crop_to_ratio(image, TARGET_RATIO)
        image = image.resize(SIZE, Image.LANCZOS)
        image = grade(image)
        path = OUT / entry["file"]
        image.save(path, "JPEG", quality=QUALITY, optimize=True, progressive=True)
        print(f"wrote {path.relative_to(ROOT)} ({path.stat().st_size // 1024} KB)")

    credits_path = OUT / "CREDITS.md"
    credits_path.write_text(credits(PHOTOS), encoding="utf-8")
    print(f"wrote {credits_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
