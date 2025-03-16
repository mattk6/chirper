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

// Script to embed the reply form benith the targeted chirp
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.reply-link').forEach(link => {
        link.addEventListener('click', event => {
            event.preventDefault(); // Prevent the default link behavior
            const chirpId = event.target.getAttribute('data-chirp-id'); // Get the chirp ID
            const replyForm = document.getElementById(`reply-form-container-${chirpId}`);

            // Toggle visibility
            if (replyForm.style.display === 'none') {
                replyForm.style.display = 'block';
            } else {
                replyForm.style.display = 'none';
            }
        });
    });
});

document.addEventListener('htmx:configRequest', (event) => {
    event.detail.headers['X-CSRFToken'] = document.querySelector('[name=csrfmiddlewaretoken]').value;
});
