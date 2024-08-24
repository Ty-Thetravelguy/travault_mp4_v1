window.onscroll = function() {
    adjustNavbar();
};

function adjustNavbar() {
    const navbar = document.querySelector(".home-nav");
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
        navbar.classList.add("navbar-scrolled");
    } else {
        navbar.classList.remove("navbar-scrolled");
    }
}
