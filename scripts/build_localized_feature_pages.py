#!/usr/bin/env python3
"""Generate localized feature guides from validated locale content files."""

from __future__ import annotations

import html
import json
from pathlib import Path

from build_feature_pages import APP_STORE, FEATURES, icon, svg_sprite


ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "content" / "feature-guides"

LANGUAGE_LINKS = [
    ("en", "/", "en", "English"),
    ("de", "/de/", "de", "Deutsch"),
    ("fr", "/fr/", "fr", "Français"),
    ("es", "/es/", "es", "Español"),
    ("it", "/it/", "it", "Italiano"),
    ("nl", "/nl/", "nl", "Nederlands"),
    ("pt-br", "/pt-br/", "pt-BR", "Português (Brasil)"),
    ("pt-pt", "/pt-pt/", "pt-PT", "Português (Portugal)"),
    ("pl", "/pl/", "pl", "Polski"),
    ("tr", "/tr/", "tr", "Türkçe"),
    ("zh-hans", "/zh-hans/", "zh-Hans", "简体中文"),
    ("ja", "/ja/", "ja", "日本語"),
    ("ko", "/ko/", "ko", "한국어"),
    ("hi", "/hi/", "hi", "हिन्दी"),
]


def load_locales() -> dict[str, dict]:
    locales: dict[str, dict] = {}
    if not CONTENT_DIR.exists():
        return locales
    for path in sorted(CONTENT_DIR.glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        locale = payload["locale"]
        if locale != path.stem:
            raise ValueError(f"{path}: locale must match the filename")
        if set(payload["features"]) != set(FEATURES):
            missing = sorted(set(FEATURES) - set(payload["features"]))
            extra = sorted(set(payload["features"]) - set(FEATURES))
            raise ValueError(f"{path}: feature mismatch; missing={missing}, extra={extra}")
        locales[locale] = payload
    return locales


def feature_path(locale: str, slug: str) -> str:
    return f"/{slug}/" if locale == "en" else f"/{locale}/{slug}/"


def feature_url(locale: str, slug: str) -> str:
    return f"https://proscanpdf.com{feature_path(locale, slug)}"


def merged_features(payload: dict) -> dict[str, dict]:
    return {
        slug: {**english_item, **payload["features"][slug]}
        for slug, english_item in FEATURES.items()
    }


def alternate_links(slug: str, payloads: dict[str, dict]) -> str:
    lines = [
        f'    <link rel="alternate" hreflang="en" href="{feature_url("en", slug)}">'
    ]
    for payload in payloads.values():
        lines.append(
            f'    <link rel="alternate" hreflang="{payload["hreflang"]}" href="{feature_url(payload["locale"], slug)}">'
        )
    lines.append(
        f'    <link rel="alternate" hreflang="x-default" href="{feature_url("en", slug)}">'
    )
    return "\n".join(lines)


def json_ld(slug: str, item: dict, payload: dict) -> str:
    locale = payload["locale"]
    ui = payload["ui"]
    canonical = feature_url(locale, slug)
    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": f"{canonical}#webpage",
                "url": canonical,
                "name": item["title"],
                "description": item["description"],
                "inLanguage": payload["hreflang"],
                "isPartOf": {"@id": "https://proscanpdf.com/#website"},
                "about": {"@id": "https://proscanpdf.com/#app"},
                "dateModified": "2026-08-22",
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": ui["home"],
                        "item": f"https://proscanpdf.com{payload['home_url']}",
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": item["heading"].replace("\n", " "),
                        "item": canonical,
                    },
                ],
            },
            {
                "@type": "HowTo",
                "name": item["heading"].replace("\n", " "),
                "description": item["lead"],
                "inLanguage": payload["hreflang"],
                "step": [
                    {"@type": "HowToStep", "position": index, "name": title, "text": text}
                    for index, (title, text) in enumerate(item["steps"], 1)
                ],
            },
            {
                "@type": "FAQPage",
                "inLanguage": payload["hreflang"],
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": question,
                        "acceptedAnswer": {"@type": "Answer", "text": answer},
                    }
                    for question, answer in item["faqs"]
                ],
            },
            {
                "@type": "MobileApplication",
                "@id": "https://proscanpdf.com/#app",
                "name": "ProScan PDF",
                "url": "https://proscanpdf.com/",
                "downloadUrl": APP_STORE,
                "applicationCategory": "BusinessApplication",
                "operatingSystem": "iOS, iPadOS",
                "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
            },
            {
                "@type": "Organization",
                "@id": "https://proscanpdf.com/#organization",
                "name": "ProScan PDF",
                "url": "https://proscanpdf.com/",
                "logo": {"@type": "ImageObject", "url": "https://proscanpdf.com/appicon.png"},
                "sameAs": [APP_STORE, "https://paulcrp.com/"],
            },
            {
                "@type": "WebSite",
                "@id": "https://proscanpdf.com/#website",
                "url": "https://proscanpdf.com/",
                "name": "ProScan PDF",
                "publisher": {"@id": "https://proscanpdf.com/#organization"},
            },
        ],
    }
    return json.dumps(graph, ensure_ascii=False, indent=6)


def render_page(
    slug: str,
    item: dict,
    payload: dict,
    payloads: dict[str, dict],
    localized_features: dict[str, dict],
) -> str:
    locale = payload["locale"]
    ui = payload["ui"]
    canonical = feature_url(locale, slug)
    asset_locale = payload.get("asset_locale")
    asset_root = f"/assets/{asset_locale}" if asset_locale else "/assets"
    heading_parts = [html.escape(part) for part in item["heading"].split("\n")]
    heading = heading_parts[0] if len(heading_parts) == 1 else f'{heading_parts[0]}<br><span>{" ".join(heading_parts[1:])}</span>'

    language_options = []
    available_locales = set(payloads)
    for locale_key, homepage, hreflang, label in LANGUAGE_LINKS:
        if locale_key == "en":
            href = feature_path("en", slug)
        elif locale_key in available_locales:
            href = feature_path(locale_key, slug)
        else:
            href = homepage
        current = ' aria-current="page"' if locale_key == locale else ""
        language_options.append(
            f'                        <a href="{href}" lang="{hreflang}" hreflang="{hreflang}"{current}>{label}</a>'
        )
    language_options_html = "\n".join(language_options)

    chips = "".join(f'<span>{icon("check")}{html.escape(label)}</span>' for label in item["chips"])
    proofs = "\n".join(
        f'''                <article class="guide-proof reveal">
                    <div class="guide-icon">{icon(symbol)}</div>
                    <h2>{html.escape(title)}</h2>
                    <p>{html.escape(text)}</p>
                </article>'''
        for symbol, title, text in item["proofs"]
    )
    steps = "\n".join(
        f'''                <article class="guide-step reveal">
                    <span class="guide-step-number">{index:02d}</span>
                    <h3>{html.escape(title)}</h3>
                    <p>{html.escape(text)}</p>
                </article>'''
        for index, (title, text) in enumerate(item["steps"], 1)
    )
    details = "\n".join(
        f'''                <article class="guide-detail reveal">
                    <h2>{html.escape(title)}</h2>
                    <p>{html.escape(text)}</p>
                </article>'''
        for title, text in item["details"]
    )
    faqs = "\n".join(
        f'<details><summary>{html.escape(question)}<span aria-hidden="true"></span></summary><p>{html.escape(answer)}</p></details>'
        for question, answer in item["faqs"]
    )
    related = "\n".join(
        f'''                <a class="related-guide reveal" href="{feature_path(locale, related_slug)}">
                    <div class="guide-icon">{icon(localized_features[related_slug]["icon"])}</div>
                    <h3>{html.escape(localized_features[related_slug]["heading"].replace(chr(10), " "))}</h3>
                    <p>{html.escape(localized_features[related_slug]["lead"])}</p>
                </a>'''
        for related_slug in item["related"]
    )
    alternate_html = alternate_links(slug, payloads)
    homepage = payload["home_url"]
    image_src = f'{asset_root}/{item["image"]}.webp'
    image_srcset = (
        f'{asset_root}/{item["image"]}-360.webp 360w, '
        f'{asset_root}/{item["image"]}-540.webp 540w, '
        f'{asset_root}/{item["image"]}.webp 720w'
    )
    badge = f'/assets/{payload["app_store_badge"]}'
    footer_links = {
        "scan-to-pdf": ui["footer_scan"],
        "photo-to-pdf": ui["footer_photos"],
        "ocr-text-extraction": ui["footer_ocr"],
        "organize-pdf-pages": ui["footer_organize"],
        "pdf-to-images": ui["footer_images"],
        "add-watermark": ui["footer_watermark"],
        "pdf-compressor": ui["footer_compress"],
        "pdf-to-word": ui["footer_word"],
        "sign-pdf": ui["footer_sign"],
        "id-photo-maker": ui["footer_id"],
    }

    return f'''<!doctype html>
<html lang="{payload["hreflang"]}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
    <title>{html.escape(item["title"])}</title>
    <meta name="description" content="{html.escape(item["description"], quote=True)}">
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
    <meta name="theme-color" content="#12171B">
    <meta name="apple-itunes-app" content="app-id=6752308731">
    <link rel="canonical" href="{canonical}">
{alternate_html}
    <link rel="icon" type="image/svg+xml" href="/assets/favicon-paper-on-ink.svg?v=paper-1">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png?v=paper-1">
    <link rel="shortcut icon" href="/favicon.ico?v=paper-1">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png?v=paper-1">
    <link rel="preload" href="/assets/fonts/nunito-latin.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="preload" as="image" href="{image_src}" imagesrcset="{image_srcset}" imagesizes="(max-width: 700px) 70vw, 350px" type="image/webp">
    <link rel="stylesheet" href="/styles.min.css?v=seo-guides-4">

    <meta property="og:type" content="website">
    <meta property="og:locale" content="{payload["og_locale"]}">
    <meta property="og:site_name" content="ProScan PDF">
    <meta property="og:title" content="{html.escape(item["title"], quote=True)}">
    <meta property="og:description" content="{html.escape(item["description"], quote=True)}">
    <meta property="og:url" content="{canonical}">
    <meta property="og:image" content="https://proscanpdf.com/assets/proscan-social-card.webp">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:alt" content="{html.escape(ui["og_image_alt"], quote=True)}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{html.escape(item["title"], quote=True)}">
    <meta name="twitter:description" content="{html.escape(item["description"], quote=True)}">
    <meta name="twitter:image" content="https://proscanpdf.com/assets/proscan-social-card.webp">

    <script type="application/ld+json">
{json_ld(slug, item, payload)}
    </script>
</head>
<body class="feature-page">
    <a class="skip-link" href="#main-content">{html.escape(ui["skip_content"])}</a>
    <svg class="svg-sprite" aria-hidden="true">
{svg_sprite()}
    </svg>

    <header class="site-header" data-header>
        <nav class="nav-shell" aria-label="{html.escape(ui["main_navigation"], quote=True)}">
            <a class="brand" href="{homepage}" aria-label="{html.escape(ui["home_aria"], quote=True)}">
                <span class="brand-icon"><img src="/assets/proscan-mark.svg" alt="" width="40" height="40"></span>
                <span>ProScan PDF</span>
            </a>
            <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-menu" data-nav-toggle>
                <span></span><span></span><span></span><span class="sr-only">{html.escape(ui["open_navigation"])}</span>
            </button>
            <div class="nav-menu" id="nav-menu" data-nav-menu>
                <a href="{homepage}#scanner">{html.escape(ui["scanner"])}</a><a href="{homepage}#tools">{html.escape(ui["pdf_tools"])}</a><a href="{homepage}#privacy">{html.escape(ui["privacy"])}</a><a href="#faq">{html.escape(ui["faq"])}</a>
            </div>
            <div class="header-actions">
                <details class="language-selector" data-language-selector>
                    <summary aria-label="{payload["short_code"]} — {html.escape(ui["choose_language"], quote=True)}">{icon("language")}<span>{payload["short_code"]}</span><svg class="language-chevron" aria-hidden="true"><use href="#icon-chevron-down"></use></svg></summary>
                    <div class="language-options" aria-label="{html.escape(ui["language"], quote=True)}">
{language_options_html}
                    </div>
                </details>
                <a class="nav-cta" href="{APP_STORE}" data-app-store="navigation" rel="noopener">{html.escape(ui["get_app"])}</a>
            </div>
        </nav>
    </header>

    <main id="main-content">
        <section class="feature-hero" id="top">
            <div class="hero-noise" aria-hidden="true"></div>
            <div class="feature-hero-grid section-shell">
                <div class="feature-copy">
                    <nav class="feature-breadcrumbs" aria-label="Breadcrumb"><a href="{homepage}">ProScan PDF</a><span aria-hidden="true">/</span><span>{html.escape(item["heading"].split(chr(10))[0])}</span></nav>
                    <p class="eyebrow hero-enter">{html.escape(item["eyebrow"])}</p>
                    <h1 class="hero-enter">{heading}</h1>
                    <p class="hero-lead hero-enter">{html.escape(item["lead"])}</p>
                    <div class="feature-chip-row hero-enter">{chips}</div>
                    <a class="official-store-link hero-enter" href="{APP_STORE}" data-app-store="feature-hero" rel="noopener" aria-label="{html.escape(ui["download_aria"], quote=True)}"><img src="{badge}" width="210" height="70" alt="{html.escape(ui["download_alt"], quote=True)}"></a>
                </div>
                <div class="feature-visual hero-enter" aria-label="{html.escape(item["image_alt"], quote=True)}">
                    <div class="device feature-device"><div class="device-sensor" aria-hidden="true"></div><img src="{image_src}" srcset="{image_srcset}" sizes="(max-width: 700px) 70vw, 350px" width="720" height="1566" alt="{html.escape(item["image_alt"], quote=True)}" fetchpriority="high"></div>
                    <div class="feature-callout"><span>{icon(item["icon"])}</span><div><strong>{html.escape(item["callout_title"])}</strong><small>{html.escape(item["callout_text"])}</small></div></div>
                </div>
            </div>
        </section>

        <section class="guide-intro section-shell" aria-label="{html.escape(ui["key_benefits"], quote=True)}"><div class="guide-proof-grid">{proofs}</div></section>

        <section class="guide-section"><div class="section-shell">
            <div class="guide-section-heading reveal"><p class="eyebrow">{html.escape(ui["workflow_eyebrow"])}</p><h2>{html.escape(ui["workflow_title_1"])}<br><span>{html.escape(ui["workflow_title_2"])}</span></h2><p>{html.escape(ui["workflow_text"])}</p></div>
            <div class="guide-step-grid">{steps}</div>
        </div></section>

        <section class="guide-section"><div class="section-shell">
            <div class="guide-section-heading reveal"><p class="eyebrow">{html.escape(ui["details_eyebrow"])}</p><h2>{html.escape(ui["details_title_1"])}<br><span>{html.escape(ui["details_title_2"])}</span></h2></div>
            <div class="guide-detail-grid">{details}</div>
            <aside class="honest-note reveal">{icon("check")}<div><h2>{html.escape(item["note_title"])}</h2><p>{html.escape(item["note"])}</p></div></aside>
        </div></section>

        <section class="faq-section feature-faq guide-section" id="faq"><div class="section-shell faq-grid">
            <div class="faq-intro reveal"><p class="eyebrow">{html.escape(ui["faq_eyebrow"])}</p><h2>{html.escape(ui["faq_title_1"])}<br><span>{html.escape(ui["faq_title_2"])}</span></h2><p>{html.escape(ui["faq_text"])}</p></div>
            <div class="faq-list reveal">{faqs}</div>
        </div></section>

        <section class="guide-section"><div class="section-shell">
            <div class="guide-section-heading reveal"><p class="eyebrow">{html.escape(ui["related_eyebrow"])}</p><h2>{html.escape(ui["related_title_1"])}<br><span>{html.escape(ui["related_title_2"])}</span></h2></div>
            <div class="related-guide-grid">{related}</div>
        </div></section>

        <section class="download-section section-pad"><div class="section-shell download-card reveal">
            <div class="download-mark"><img src="/assets/proscan-mark.svg" alt="" width="104" height="104"></div>
            <p class="eyebrow">{html.escape(ui["cta_eyebrow"])}</p><h2>{html.escape(ui["cta_title_1"])}<br><span>{html.escape(ui["cta_title_2"])}</span></h2><p>{html.escape(ui["cta_text"])}</p>
            <a class="official-store-link" href="{APP_STORE}" data-app-store="final-cta" rel="noopener" aria-label="{html.escape(ui["download_aria"], quote=True)}"><img src="{badge}" width="210" height="70" alt="{html.escape(ui["download_alt"], quote=True)}"></a>
        </div></section>
    </main>

    <footer class="site-footer"><div class="section-shell footer-grid">
        <div class="footer-brand"><a class="brand" href="{homepage}"><span class="brand-icon"><img src="/assets/proscan-mark.svg" alt="" width="40" height="40"></span><span>ProScan PDF</span></a><p>{html.escape(ui["footer_description"])}</p></div>
        <div class="footer-links">
            <div><strong>{html.escape(ui["footer_product"])}</strong><a href="{feature_path(locale, 'scan-to-pdf')}">{html.escape(footer_links['scan-to-pdf'])}</a><a href="{feature_path(locale, 'photo-to-pdf')}">{html.escape(footer_links['photo-to-pdf'])}</a><a href="{feature_path(locale, 'ocr-text-extraction')}">{html.escape(footer_links['ocr-text-extraction'])}</a><a href="{feature_path(locale, 'organize-pdf-pages')}">{html.escape(footer_links['organize-pdf-pages'])}</a></div>
            <div><strong>{html.escape(ui["footer_tools"])}</strong><a href="{feature_path(locale, 'pdf-to-images')}">{html.escape(footer_links['pdf-to-images'])}</a><a href="{feature_path(locale, 'add-watermark')}">{html.escape(footer_links['add-watermark'])}</a><a href="{feature_path(locale, 'pdf-compressor')}">{html.escape(footer_links['pdf-compressor'])}</a><a href="{feature_path(locale, 'pdf-to-word')}">{html.escape(footer_links['pdf-to-word'])}</a><a href="{feature_path(locale, 'sign-pdf')}">{html.escape(footer_links['sign-pdf'])}</a><a href="{feature_path(locale, 'id-photo-maker')}">{html.escape(footer_links['id-photo-maker'])}</a></div>
            <div><strong>{html.escape(ui["footer_more"])}</strong><a href="{APP_STORE}" data-app-store="footer" rel="noopener">{html.escape(ui["app_store"])}</a><a href="https://paulcrp.com/proscanpdf_privacypolicy.html" rel="noopener">{html.escape(ui["privacy_policy"])}</a><a href="mailto:info@proscanpdf.com">{html.escape(ui["contact_support"])}</a></div>
        </div>
    </div><div class="section-shell footer-bottom"><span>© <span data-year></span> ProScan PDF</span><span>{html.escape(ui["made_for"])}</span></div></footer>
    <script src="/script.min.js?v=seo-guides-2" defer></script>
</body>
</html>
'''


def main() -> None:
    payloads = load_locales()
    page_count = 0
    for locale, payload in payloads.items():
        features = merged_features(payload)
        for slug, item in features.items():
            target = ROOT / locale / slug
            target.mkdir(parents=True, exist_ok=True)
            (target / "index.html").write_text(
                render_page(slug, item, payload, payloads, features),
                encoding="utf-8",
            )
            page_count += 1
    print(f"Generated {page_count} localized feature guides across {len(payloads)} locale(s)")


if __name__ == "__main__":
    main()
