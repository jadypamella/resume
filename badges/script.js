// Developer attribution
console.log(
    '❤️ This website was developed with love and dedication by Jady Pamella\n' +
    '🌐 Portfolio: https://jadypamella.com'
);

(function () {
    'use strict';

    // Hamburger menu toggle (mobile <= 768 currently keeps sidebar inline; toggle reserved for tablet range)
    const hamburger = document.getElementById('hamburger');
    const sidebar = document.querySelector('.sidebar');
    const sidebarOverlay = document.getElementById('sidebarOverlay');

    function toggleMenu() {
        if (!hamburger || !sidebar || !sidebarOverlay) return;
        const isActive = hamburger.classList.toggle('active');
        sidebar.classList.toggle('active');
        sidebarOverlay.classList.toggle('active');
        hamburger.setAttribute('aria-expanded', String(isActive));
        document.body.style.overflow = isActive ? 'hidden' : '';
    }

    if (hamburger) hamburger.addEventListener('click', toggleMenu);
    if (sidebarOverlay) sidebarOverlay.addEventListener('click', toggleMenu);

    // Auto-close sidebar after clicking nav links on small screens
    document.querySelectorAll('.sidebar a').forEach((link) => {
        link.addEventListener('click', () => {
            if (window.innerWidth <= 768 && sidebar && sidebar.classList.contains('active')) {
                toggleMenu();
            }
        });
    });

    // Smooth scroll for in-page anchors only
    document.addEventListener('DOMContentLoaded', () => {
        const inPageLinks = document.querySelectorAll('.nav-menu a[href^="#"]');
        inPageLinks.forEach((link) => {
            link.addEventListener('click', (event) => {
                const targetId = link.getAttribute('href');
                if (!targetId || targetId === '#') return;
                const target = document.querySelector(targetId);
                if (!target) return;
                event.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            });
        });
    });
})();
