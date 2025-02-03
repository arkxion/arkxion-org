/* static/js/language.css */
document.addEventListener("DOMContentLoaded", function () {
    const langSelector = document.querySelector(".custom-language-selector");
    const langButton = document.querySelector(".lang-btn");
    const langDropdown = document.querySelector(".lang-dropdown");

    function getCurrentLang() {
        const pathParts = window.location.pathname.split("/");
        return pathParts[1] || "en";
    }

    function updateButtonText(lang) {
        const langMap = {
            en: "🇺🇸 English (US)",
            en_uk: "🇬🇧 English (UK)",
            ja: "🇯🇵 日本語",
        };
        langButton.innerHTML = (langMap[lang] || "🌍 English (US)") + " ▼";
    }

    const currentLang = getCurrentLang();
    updateButtonText(currentLang);

    langButton.addEventListener("click", function (event) {
        event.stopPropagation();
        langSelector.classList.toggle("active");
    });

    langDropdown.addEventListener("click", function (event) {
        const selectedLang =
            event.target.closest("li")?.dataset.lang ||
            event.target.dataset.lang;
        if (selectedLang) {
            updateButtonText(selectedLang);

            const newUrl =
                `/${selectedLang}/` +
                window.location.pathname.split("/").slice(2).join("/");
            window.location.assign(newUrl);
        }
    });

    document.addEventListener("click", function () {
        langSelector.classList.remove("active");
    });
});
