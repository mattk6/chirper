// script.js
// Grant Wells

// Wait for the webpage to fully load
document.addEventListener("DOMContentLoaded", function () {
    // Select the checkbox input for toggling themes
    const themeToggle = document.getElementById("theme-toggle");

    // Toggle dark mode when the switch is clicked
    themeToggle.addEventListener("change", function () {
        document.body.classList.toggle("dark-mode");
    });
});
