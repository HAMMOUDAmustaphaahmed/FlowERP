// JS for authentication pages (login, signup)
document.addEventListener('DOMContentLoaded', function () {
    // For example: toggle password visibility
    const toggles = document.querySelectorAll('.toggle-password');
    toggles.forEach(t => {
        t.addEventListener('click', function() {
            const input = document.getElementById(this.dataset.toggle);
            if (input) input.type = input.type === 'password' ? 'text' : 'password';
        });
    });
});