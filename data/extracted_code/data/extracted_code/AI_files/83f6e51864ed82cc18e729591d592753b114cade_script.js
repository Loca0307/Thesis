const carouselNext = document.querySelector('.carousel-next');
const carouselPrev = document.querySelector('.carousel-prev');

if (carouselNext) {
  carouselNext.addEventListener('click', () => {
    currentTestimonial = (currentTestimonial + 1) % testimonials.length;
    showTestimonial(currentTestimonial);
  });
}

if (carouselPrev) {
  carouselPrev.addEventListener('click', () => {
    currentTestimonial = (currentTestimonial - 1 + testimonials.length) % testimonials.length;
    showTestimonial(currentTestimonial);
  });
if (loginForm) {
  loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = document.getElementById('email').value;
    if (!email.includes('@')) {
      const emailError = document.getElementById('email-error');
      if (emailError) {
        emailError.textContent = 'Valid email required';
      }
      return;
    }
    // Proceed with login
  });
}