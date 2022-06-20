let hamburger = document.querySelector('.hamburger');
let menu = document.querySelector('.header-nav-menu');


hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    menu.classList.toggle('active');
});