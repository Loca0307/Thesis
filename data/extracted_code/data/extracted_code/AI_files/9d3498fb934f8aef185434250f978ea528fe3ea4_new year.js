// Set the date we're counting down to
const newYearDate = new Date('December 31, 2024 23:59:59').getTime();

// Select the countdown and message elements
const daysElement = document.getElementById("days");
const hoursElement = document.getElementById("hours");
const minutesElement = document.getElementById("minutes");
const secondsElement = document.getElementById("seconds");
const countdownElement = document.getElementById('countdown');
const newYearMessage = document.getElementById('newYearMessage');

// Set up canvas for fireworks
const canvas = document.getElementById('fireworkCanvas');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Array to hold fireworks particles
const particles = [];

class Particle {
    constructor(x, y, color, velocity, size, lifespan) {
        this.x = x;
        this.y = y;
        this.color = color;
        this.velocity = velocity;
        this.size = size;
        this.lifespan = lifespan;
        this.age = 0;
    }

    draw() {
        ctx.save();
        ctx.globalAlpha = Math.max(1 - this.age / this.lifespan, 0);
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fillStyle = this.color;
        ctx.fill();
        ctx.restore();
    }

    update() {
        this.x += this.velocity.x;
        this.y += this.velocity.y;
        this.velocity.y += 0.05; // Simulate gravity
        this.size *= 0.98; // Shrink over time
        this.age++;
    }

    isExpired() {
        return this.age > this.lifespan;
    }
}

function createFirework(x, y) {
    const colors = ["#ff6f61", "#ffc107", "#8e44ad", "#3498db", "#2ecc71", "#f39c12", "#e74c3c"];
    const baseColor = colors[Math.floor(Math.random() * colors.length)];

    for (let i = 0; i < 100; i++) {
        const angle = Math.random() * Math.PI * 2;
        const speed = Math.random() * 4 + 2;
        const velocity = {
            x: Math.cos(angle) * speed,
            y: Math.sin(angle) * speed
        };
        const size = Math.random() * 3 + 2;
        const lifespan = Math.random() * 40 + 60;

        particles.push(new Particle(x, y, baseColor, velocity, size, lifespan));
    }
}

function randomFireworks() {
    const x = Math.random() * canvas.width;
    const y = Math.random() * canvas.height * 0.5; // Fireworks originate from the upper half of the screen
    createFirework(x, y);
}

function animateFireworks() {
    ctx.fillStyle = "rgba(0, 0, 0, 0.2)";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    particles.forEach((particle, index) => {
        if (particle.isExpired()) {
            particles.splice(index, 1);
        } else {
            particle.update();
            particle.draw();
        }
    });

    if (Math.random() < 0.05) {
        randomFireworks();
    }

    requestAnimationFrame(animateFireworks);
}

// Countdown logic
const countdownInterval = setInterval(() => {
    const now = new Date().getTime();
    const timeLeft = newYearDate - now;

    if (timeLeft <= 0) {
        clearInterval(countdownInterval);
        countdownElement.style.display = 'none'; // Hide the countdown
        newYearMessage.style.display = 'block'; // Show the New Year message
        animateFireworks(); // Start fireworks animation
        return;
    }

    const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

    daysElement.textContent = days.toString().padStart(2, '0');
    hoursElement.textContent = hours.toString().padStart(2, '0');
    minutesElement.textContent = minutes.toString().padStart(2, '0');
    secondsElement.textContent = seconds.toString().padStart(2, '0');
}, 1000);

// Resize canvas on window resize
window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});