document.addEventListener('DOMContentLoaded', function() {
    const navbar = document.querySelector(".home-nav");
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    const sections = document.querySelectorAll('section');

    // Check if the current page is the home page
    const isHomePage = window.location.pathname === '/';  // Adjust this if your home page has a different URL

    // Smooth scrolling or page navigation
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');

            if (targetId.startsWith('#') && isHomePage) {
                e.preventDefault();
                const targetSection = document.querySelector(targetId);
                if (targetSection) {
                    const navbarHeight = navbar.offsetHeight;
                    const targetPosition = targetSection.getBoundingClientRect().top + window.pageYOffset - navbarHeight;
                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });
                }
            } else if (targetId.startsWith('#') && !isHomePage) {
                // If not on the home page, navigate back to home and then to the correct section
                e.preventDefault();
                window.location.href = '/' + targetId;  // Assuming '/' is the home page URL
            }
        });
    });

    // Combine scroll events
    window.onscroll = function() {
        if (isHomePage) {
            adjustNavbar();
            updateActiveLink();
        }
    };

    function adjustNavbar() {
        if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
            navbar.classList.add("navbar-scrolled");
        } else {
            navbar.classList.remove("navbar-scrolled");
        }
    }

    function updateActiveLink() {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (window.scrollY >= sectionTop - sectionHeight / 3) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            if (link.getAttribute('href').startsWith('#')) {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${current}`) {
                    link.classList.add('active');
                }
            }
        });
    }
});
