/* static/js/header.css */
document.addEventListener("DOMContentLoaded", () => {
    const menuToggle = document.querySelector(".menu-toggle");
    const menuContainer = document.querySelector(".menu-container");

    menuToggle.addEventListener("click", () => {
        const isActive = menuContainer.classList.toggle("active");
        menuToggle.setAttribute("aria-expanded", isActive);
        menuToggle.innerHTML = isActive ? "&#x2715;" : "&#9776;";
    });

    document.addEventListener("click", (e) => {
        if (
            !menuContainer.contains(e.target) &&
            !menuToggle.contains(e.target)
        ) {
            menuContainer.classList.remove("active");
            menuToggle.setAttribute("aria-expanded", "false");
            menuToggle.innerHTML = "&#9776;";
        }
    });
});
