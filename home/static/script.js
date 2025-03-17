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
        // Add an event listener to each reply link
        link.addEventListener('click', event => {
            // Prevent the link from navigating to a new page
            event.preventDefault(); 
            // Get set the chirp id from the data attribute and get the reply form
            const chirpId = event.target.getAttribute('data-chirp-id'); 
            const replyForm = document.getElementById(`reply-form-container-${chirpId}`);

            // Toggle the display of the reply form
            if (replyForm.style.display === 'none') {
                // Display the reply form
                replyForm.style.display = 'block';
            } else {
                // Hide the reply form
                replyForm.style.display = 'none';
            }
        });
    });
});

// Add CSRF token to all htmx requests
document.addEventListener('htmx:configRequest', (event) => {
    event.detail.headers['X-CSRFToken'] = document.querySelector('[name=csrfmiddlewaretoken]').value;
});
