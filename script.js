document.documentElement.classList.add("js");

const analyticsPreferenceKey = "proscanpdf-analytics-consent-v1";
const analyticsMeasurementId = "G-6B1X79SYTC";
let analyticsLoadStarted = false;

const consentTranslations = {
    en: {
        copy: "We use optional analytics to understand which pages are useful. No advertising cookies.",
        decline: "Not now",
        accept: "Allow analytics",
        privacy: "Privacy policy"
    },
    de: {
        copy: "Optionale Analysen helfen uns zu verstehen, welche Seiten nützlich sind. Keine Werbe-Cookies.",
        decline: "Nicht jetzt",
        accept: "Analysen erlauben",
        privacy: "Datenschutz"
    },
    es: {
        copy: "Usamos análisis opcionales para saber qué páginas resultan útiles. Sin cookies publicitarias.",
        decline: "Ahora no",
        accept: "Permitir análisis",
        privacy: "Privacidad"
    },
    fr: {
        copy: "Des statistiques facultatives nous aident à comprendre quelles pages sont utiles. Aucun cookie publicitaire.",
        decline: "Pas maintenant",
        accept: "Autoriser",
        privacy: "Confidentialité"
    },
    it: {
        copy: "Le statistiche facoltative ci aiutano a capire quali pagine sono utili. Nessun cookie pubblicitario.",
        decline: "Non ora",
        accept: "Consenti analisi",
        privacy: "Privacy"
    },
    nl: {
        copy: "Optionele analyses helpen ons begrijpen welke pagina's nuttig zijn. Geen advertentiecookies.",
        decline: "Niet nu",
        accept: "Analyse toestaan",
        privacy: "Privacy"
    },
    pl: {
        copy: "Opcjonalne statystyki pomagają nam sprawdzić, które strony są przydatne. Bez reklamowych plików cookie.",
        decline: "Nie teraz",
        accept: "Zezwól na analizę",
        privacy: "Prywatność"
    },
    pt: {
        copy: "A análise opcional ajuda-nos a perceber que páginas são úteis. Sem cookies de publicidade.",
        decline: "Agora não",
        accept: "Permitir análise",
        privacy: "Privacidade"
    },
    tr: {
        copy: "İsteğe bağlı analizler hangi sayfaların yararlı olduğunu anlamamıza yardımcı olur. Reklam çerezi yoktur.",
        decline: "Şimdi değil",
        accept: "Analize izin ver",
        privacy: "Gizlilik"
    },
    zh: {
        copy: "可选的分析数据可帮助我们了解哪些页面更有用。不使用广告 Cookie。",
        decline: "暂不",
        accept: "允许分析",
        privacy: "隐私政策"
    },
    ja: {
        copy: "任意のアクセス解析は、役立つページの把握に使用します。広告 Cookie は使用しません。",
        decline: "今はしない",
        accept: "解析を許可",
        privacy: "プライバシー"
    },
    ko: {
        copy: "가치 있는 페이지를 파악하기 위해 선택적 분석을 사용합니다. 광고 쿠키는 사용하지 않습니다.",
        decline: "나중에",
        accept: "분석 허용",
        privacy: "개인정보"
    },
    hi: {
        copy: "वैकल्पिक एनालिटिक्स से हमें समझने में मदद मिलती है कि कौन-से पेज उपयोगी हैं। कोई विज्ञापन कुकी नहीं।",
        decline: "अभी नहीं",
        accept: "अनुमति दें",
        privacy: "गोपनीयता"
    }
};

function analyticsLanguage() {
    const language = document.documentElement.lang.toLowerCase();
    if (language.startsWith("pt")) return "pt";
    if (language.startsWith("zh")) return "zh";
    return language.split("-")[0];
}

function loadGoogleAnalytics() {
    if (analyticsLoadStarted) return;
    analyticsLoadStarted = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function gtag(){ window.dataLayer.push(arguments); };
    window.gtag("js", new Date());
    window.gtag("config", analyticsMeasurementId, {
        anonymize_ip: true,
        allow_google_signals: false,
        allow_ad_personalization_signals: false
    });

    const analyticsScript = document.createElement("script");
    analyticsScript.async = true;
    analyticsScript.src = `https://www.googletagmanager.com/gtag/js?id=${analyticsMeasurementId}`;
    document.head.appendChild(analyticsScript);
}

function loadAnalyticsWhenIdle() {
    if ("requestIdleCallback" in window) {
        window.requestIdleCallback(loadGoogleAnalytics, { timeout: 2500 });
    } else {
        window.setTimeout(loadGoogleAnalytics, 1200);
    }
}

function saveAnalyticsPreference(value) {
    try {
        window.localStorage.setItem(analyticsPreferenceKey, value);
    } catch (_) {
        // The choice remains valid for this page when storage is unavailable.
    }
}

function showConsentBanner() {
    const copy = consentTranslations[analyticsLanguage()] || consentTranslations.en;
    const banner = document.createElement("aside");
    banner.className = "consent-banner";
    banner.setAttribute("aria-label", copy.privacy);
    banner.innerHTML = `
        <p class="consent-copy">${copy.copy} <a href="https://paulcrp.com/proscanpdf_privacypolicy.html" rel="noopener">${copy.privacy}</a></p>
        <div class="consent-actions">
            <button class="consent-button consent-button-secondary" type="button" data-consent-decline>${copy.decline}</button>
            <button class="consent-button consent-button-primary" type="button" data-consent-accept>${copy.accept}</button>
        </div>`;
    document.body.appendChild(banner);

    banner.querySelector("[data-consent-decline]")?.addEventListener("click", () => {
        saveAnalyticsPreference("declined");
        banner.remove();
    });
    banner.querySelector("[data-consent-accept]")?.addEventListener("click", () => {
        saveAnalyticsPreference("accepted");
        banner.remove();
        loadAnalyticsWhenIdle();
    });
}

let savedAnalyticsPreference = null;
try {
    savedAnalyticsPreference = window.localStorage.getItem(analyticsPreferenceKey);
} catch (_) {}

if (savedAnalyticsPreference === "accepted") {
    loadAnalyticsWhenIdle();
} else if (savedAnalyticsPreference !== "declined") {
    window.setTimeout(showConsentBanner, 650);
}

const header = document.querySelector("[data-header]");
const navToggle = document.querySelector("[data-nav-toggle]");
const navMenu = document.querySelector("[data-nav-menu]");
const languageSelectors = document.querySelectorAll("[data-language-selector]");
const languagePreferenceKey = "proscanpdf-language-path";
const supportedLanguagePaths = new Set([
    "/", "/de/", "/fr/", "/es/", "/it/", "/nl/", "/pt-br/",
    "/pt-pt/", "/pl/", "/tr/", "/zh-hans/", "/ja/", "/ko/", "/hi/"
]);

function setMenuOpen(isOpen) {
    if (!navToggle || !navMenu) return;
    navToggle.setAttribute("aria-expanded", String(isOpen));
    navMenu.classList.toggle("is-open", isOpen);
}

navToggle?.addEventListener("click", () => {
    const willOpen = navToggle.getAttribute("aria-expanded") !== "true";
    if (willOpen) languageSelectors.forEach((selector) => selector.removeAttribute("open"));
    setMenuOpen(willOpen);
});

navMenu?.addEventListener("click", (event) => {
    if (event.target.closest("a")) setMenuOpen(false);
});

document.addEventListener("click", (event) => {
    languageSelectors.forEach((selector) => {
        if (!selector.contains(event.target)) selector.removeAttribute("open");
    });
    if (!navMenu?.classList.contains("is-open")) return;
    if (!event.target.closest(".nav-shell")) setMenuOpen(false);
});

document.addEventListener("keydown", (event) => {
    if (event.key !== "Escape") return;
    setMenuOpen(false);
    languageSelectors.forEach((selector) => selector.removeAttribute("open"));
});

languageSelectors.forEach((selector) => {
    selector.addEventListener("toggle", () => {
        if (!selector.open) return;
        setMenuOpen(false);
        languageSelectors.forEach((otherSelector) => {
            if (otherSelector !== selector) otherSelector.removeAttribute("open");
        });
    });

    selector.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", () => {
            const selectedPath = new URL(link.href, window.location.href).pathname;
            if (!supportedLanguagePaths.has(selectedPath)) return;
            try {
                window.localStorage.setItem(languagePreferenceKey, selectedPath);
            } catch (_) {}
        });
    });
});

if (header) {
    const headerSentinel = document.createElement("span");
    headerSentinel.className = "header-sentinel";
    headerSentinel.setAttribute("aria-hidden", "true");
    document.body.prepend(headerSentinel);

    if ("IntersectionObserver" in window) {
        const headerObserver = new IntersectionObserver(([entry]) => {
            header.classList.toggle("is-scrolled", !entry.isIntersecting);
        }, { rootMargin: "-24px 0px 0px 0px", threshold: 0 });
        headerObserver.observe(headerSentinel);
    }
}

const revealItems = document.querySelectorAll(".reveal");
if ("IntersectionObserver" in window) {
    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach((entry) => {
            if (!entry.isIntersecting) return;
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
        });
    }, { rootMargin: "0px 0px -8%", threshold: 0.08 });

    revealItems.forEach((item) => revealObserver.observe(item));
} else {
    revealItems.forEach((item) => item.classList.add("is-visible"));
}

document.querySelectorAll(".faq-list details").forEach((detail) => {
    detail.addEventListener("toggle", () => {
        if (!detail.open) return;
        document.querySelectorAll(".faq-list details[open]").forEach((openDetail) => {
            if (openDetail !== detail) openDetail.open = false;
        });
    });
});

document.querySelectorAll("[data-app-store]").forEach((link) => {
    link.addEventListener("click", () => {
        if (typeof window.gtag !== "function") return;
        window.gtag("event", "click", {
            event_category: "App Store Download",
            event_label: link.dataset.appStore
        });
    });
});

document.querySelectorAll("a[href^='http']").forEach((link) => {
    if (link.hasAttribute("data-app-store")) return;
    link.addEventListener("click", () => {
        if (typeof window.gtag !== "function") return;
        window.gtag("event", "outbound_click", {
            destination: link.href
        });
    });
});

document.querySelectorAll("[data-year]").forEach((node) => {
    node.textContent = new Date().getFullYear();
});
