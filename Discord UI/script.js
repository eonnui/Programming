document.addEventListener("DOMContentLoaded", function() {
    const container = document.querySelector(".logo-container");

    function updateFades() {
        const atTop = container.scrollTop === 0;
        const atBottom = container.scrollHeight - container.scrollTop === container.clientHeight;

        container.classList.toggle("scrolled", !atTop);
        container.classList.toggle("at-bottom", atBottom);
    }
    container.addEventListener("scroll", updateFades);
    updateFades();
});