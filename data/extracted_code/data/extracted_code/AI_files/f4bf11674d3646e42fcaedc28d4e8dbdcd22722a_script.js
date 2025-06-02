// Close menu when clicking a link
navLinks.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    menuToggle.classList.remove('active');
    navLinks.classList.remove('show');
    mobileFooter.classList.remove('show');
    body.classList.remove('menu-open');
  });
});

// Reset mobile menu state on window resize
window.addEventListener('resize', () => {
  if (window.innerWidth > 768) {
    menuToggle.classList.remove('active');
    navLinks.classList.remove('show');
    mobileFooter.classList.remove('show');
    body.classList.remove('menu-open');
  }
});
