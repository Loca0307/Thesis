// Define fade-in and fade-out animations
const fadeIn = [
  { opacity: 0 },
  { opacity: 1 }
];

const fadeOut = [
  { opacity: 1 },
  { opacity: 0 }
];

const fadeTiming = {
  duration: 200, // Adjust the duration as needed
  iterations: 1
};

// when scroll down 30px from top, show the button with fade-in animation
window.onscroll = function () {
  scrollFunction();
};