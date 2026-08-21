document.documentElement.classList.add("js");

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

let scrollFrame = 0;
function updateHeader() {
    header?.classList.toggle("is-scrolled", window.scrollY > 24);
    scrollFrame = 0;
}

window.addEventListener("scroll", () => {
    if (!scrollFrame) scrollFrame = requestAnimationFrame(updateHeader);
}, { passive: true });
updateHeader();

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
