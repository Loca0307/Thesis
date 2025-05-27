});

// Add dynamic background gradient for the photo wall
let fadeTimeout;
photoWall.addEventListener("mousemove", (event) => {
    const { clientX, clientY, currentTarget } = event;
    const { width, height, left, top } = currentTarget.getBoundingClientRect();
    const xPercent = ((clientX - left) / width) * 100;
    const yPercent = ((clientY - top) / height) * 100;

    // Update the background gradient based on the cursor's position
    photoWall.style.background = `radial-gradient(circle at ${xPercent}% ${yPercent}%, #ff7eb3, #ff758c, #ff6a6a)`;

    // Clear any existing fade timeout
    clearTimeout(fadeTimeout);

    // Set a timeout to fade the gradient when the cursor stops moving
    fadeTimeout = setTimeout(() => {
        photoWall.style.transition = "background 0.8s ease"; // Smooth fade transition
        photoWall.style.background = `radial-gradient(circle at ${xPercent}% ${yPercent}%, white, #ff758c, #ff7eb3)`;
    }, 300); // 300ms delay before fading
});

// Function to randomly swap two images in the active set
function swapRandomImages() {
    // Select the active set
    const activeSet = document.querySelector(".photo-wall.set.active");

    if (!activeSet) return; // Ensure there is an active set

    // Select all images within the active set
    const images = activeSet.querySelectorAll("img");

    if (images.length < 2) return; // Ensure there are at least two images to swap

    // Select two random images
    const firstIndex = Math.floor(Math.random() * images.length);
    let secondIndex;
    do {
        secondIndex = Math.floor(Math.random() * images.length);
    } while (secondIndex === firstIndex); // Ensure the two indices are different

    const firstImage = images[firstIndex];
    const secondImage = images[secondIndex];

    // Add fade-out effect
    firstImage.style.transition = "opacity 0.5s ease";
    secondImage.style.transition = "opacity 0.5s ease";
    firstImage.style.opacity = "0";
    secondImage.style.opacity = "0";

    // After fade-out, swap positions and fade back in
    setTimeout(() => {
        // Swap the actual DOM positions
        const parent = firstImage.parentNode;
        parent.insertBefore(secondImage, firstImage);

        // Fade back in
        firstImage.style.opacity = "1";
        secondImage.style.opacity = "1";
    }, 500); // Match the duration of the fade-out effect
}

// Set an interval to swap images every 3-5 seconds in the active set
setInterval(() => {
    swapRandomImages();
}, Math.random() * 2000 + 3000); // Random interval between 3-5 seconds

// Carousel Functionality
const sets = document.querySelectorAll(".photo-wall.set"); // Select all sets
const rightArrow = document.querySelector(".carousel-arrow.right-arrow"); // Select the right arrow button

let currentSetIndex = 0; // Track the current set index

// Function to show the current set
function showSet(index) {
    sets.forEach((set, i) => {
        set.classList.toggle("active", i === index); // Show the active set, hide others
    });
}

// Show the first set initially
showSet(currentSetIndex);

// Handle Right Arrow Click
rightArrow.addEventListener("click", () => {
    currentSetIndex = (currentSetIndex + 1) % sets.length; // Move to the next set, loop back to the start
    showSet(currentSetIndex); // Update the visible set