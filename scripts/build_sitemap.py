#!/usr/bin/env python3
"""Build the localized HTML and image sitemap."""

import json
from pathlib import Path
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1]
BASE = "https://proscanpdf.com"
LAST_MODIFIED = "2026-08-22"
LOCALIZED_FEATURE_DIR = ROOT / "content" / "feature-guides"

LANGUAGES = [
    ("en", "/", ""),
    ("de", "/de/", "de/"),
    ("fr", "/fr/", "fr/"),
    ("es", "/es/", "es/"),
    ("it", "/it/", "it/"),
    ("nl", "/nl/", "nl/"),
    ("pt-BR", "/pt-br/", "pt-br/"),
    ("pt-PT", "/pt-pt/", "pt-pt/"),
    ("pl", "/pl/", "pl/"),
    ("tr", "/tr/", "tr/"),
    ("zh-Hans", "/zh-hans/", "zh-hans/"),
    ("ja", "/ja/", "ja/"),
    ("ko", "/ko/", "ko/"),
    ("hi", "/hi/", "hi/"),
]

SCREEN_CAPTIONS = {
    "screen-home": "ProScan PDF home screen and scanning modes",
    "screen-scan": "Document scanning interface",
    "screen-tools": "PDF tools in ProScan PDF",
    "screen-files": "My Files document library",
    "screen-organize": "Organize PDF pages",
    "screen-sign": "PDF signature and form tools",
    "screen-ocr": "Live OCR text recognition",
}

FEATURES = {
    "/scan-to-pdf/": ("screen-scan", "Scan documents to PDF on iPhone and iPad"),
    "/photo-to-pdf/": ("screen-tools", "Convert one or more photos to PDF"),
    "/pdf-to-images/": ("screen-tools", "Convert every PDF page to a JPG image"),
    "/add-watermark/": ("screen-tools", "Add a colored text watermark to PDF pages"),
    "/pdf-compressor/": ("screen-tools", "Compress scanned and image-based PDF files"),
    "/sign-pdf/": ("screen-sign", "Add signatures and text form boxes to PDF files"),
    "/pdf-to-word/": ("screen-tools", "Convert PDF files to editable Word documents"),
    "/id-photo-maker/": ("screen-tools", "Create passport and ID photos"),
    "/ocr-text-extraction/": ("screen-ocr", "Extract text and create searchable PDFs"),
    "/organize-pdf-pages/": ("screen-organize", "Extract, reorder, insert, delete and merge PDF pages"),
}


def image_entry(path: str, caption: str) -> str:
    return (
        "    <image:image>\n"
        f"      <image:loc>{escape(BASE + path)}</image:loc>\n"
        f"      <image:caption>{escape(caption)}</image:caption>\n"
        "    </image:image>"
    )


def localized_url(language: str, path: str, asset_prefix: str) -> str:
    lines = ["  <url>", f"    <loc>{BASE}{path}</loc>"]
    for alternate_language, alternate_path, _ in LANGUAGES:
        lines.append(
            f'    <xhtml:link rel="alternate" hreflang="{alternate_language}" href="{BASE}{alternate_path}" />'
        )
    lines.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE}/" />')
    lines.extend([
        f"    <lastmod>{LAST_MODIFIED}</lastmod>",
        "    <changefreq>monthly</changefreq>",
        f"    <priority>{'1.0' if language == 'en' else '0.9'}</priority>",
    ])
    for screen, caption in SCREEN_CAPTIONS.items():
        lines.append(image_entry(f"/assets/{asset_prefix}{screen}.webp", caption))
    lines.append("  </url>")
    return "\n".join(lines)


def load_feature_locales() -> dict[str, dict]:
    payloads = {}
    if not LOCALIZED_FEATURE_DIR.exists():
        return payloads
    for path in sorted(LOCALIZED_FEATURE_DIR.glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        payloads[payload["locale"]] = payload
    return payloads


def localized_feature_path(locale: str, path: str) -> str:
    return path if locale == "en" else f"/{locale}{path}"


def feature_url(
    path: str,
    screen: str,
    caption: str,
    locale: str,
    payloads: dict[str, dict],
) -> str:
    localized_path = localized_feature_path(locale, path)
    lines = [
        "  <url>",
        f"    <loc>{BASE}{localized_path}</loc>",
        f'    <xhtml:link rel="alternate" hreflang="en" href="{BASE}{path}" />',
    ]
    for payload in payloads.values():
        alternate_path = localized_feature_path(payload["locale"], path)
        lines.append(
            f'    <xhtml:link rel="alternate" hreflang="{payload["hreflang"]}" href="{BASE}{alternate_path}" />'
        )
    lines.extend([
        f'    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE}{path}" />',
        f"    <lastmod>{LAST_MODIFIED}</lastmod>",
        "    <changefreq>monthly</changefreq>",
        f"    <priority>{'0.85' if locale == 'en' else '0.8'}</priority>",
    ])
    asset_prefix = "" if locale == "en" else f"{payloads[locale].get('asset_locale', locale)}/"
    lines.append(image_entry(f"/assets/{asset_prefix}{screen}.webp", caption))
    lines.append("  </url>")
    return "\n".join(lines)


def main() -> None:
    feature_locales = load_feature_locales()
    items = [localized_url(*language) for language in LANGUAGES]
    for path, (screen, caption) in FEATURES.items():
        items.append(feature_url(path, screen, caption, "en", feature_locales))
        slug = path.strip("/")
        for locale, payload in feature_locales.items():
            localized_caption = payload["features"][slug]["image_alt"]
            items.append(feature_url(path, screen, localized_caption, locale, feature_locales))
    sitemap = "\n".join([
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml"',
        '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">',
        *items,
        "</urlset>",
        "",
    ])
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    print(f"Generated sitemap with {len(items)} URLs")


if __name__ == "__main__":
    main()
