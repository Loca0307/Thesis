document.getElementById('createTimers').addEventListener('click', function() {
    const numTimers = parseInt(document.getElementById('numTimers').value);
    const defaultTime = parseInt(document.getElementById('defaultTime').value);
    const timersContainer = document.getElementById('timersContainer');
    timersContainer.innerHTML = '';

    for (let i = 1; i <= numTimers; i++) {
        const timerDiv = document.createElement('div');
        timerDiv.className = 'timer';
        timerDiv.innerHTML = `
            <input type="text" value="${i}">
            <div class="time">${defaultTime}</div>
            <div class="buttons">
                <button class="start">Start</button>
                <button class="pause">Pause</button>
                <button class="reset">Reset</button>
            </div>
        `;
        timersContainer.appendChild(timerDiv);

        const timeDisplay = timerDiv.querySelector('.time');
        let timeLeft = defaultTime;
        let interval;

        timerDiv.querySelector('.start').addEventListener('click', function() {
            if (interval) return;
            interval = setInterval(() => {
                if (timeLeft > 0) {
                    timeLeft--;
                    timeDisplay.textContent = timeLeft;
                    if (timeLeft <= 10) {
                        timeDisplay.classList.add('warning');
                    }
                } else {
                    clearInterval(interval);
                    timeDisplay.textContent = 'Times Up!';
                }
            }, 1000);
        });

        timerDiv.querySelector('.pause').addEventListener('click', function() {
            clearInterval(interval);
            interval = null;
        });

        timerDiv.querySelector('.reset').addEventListener('click', function() {
            clearInterval(interval);
            interval = null;
            timeLeft = defaultTime;
            timeDisplay.textContent = timeLeft;
            timeDisplay.classList.remove('warning');
        });
    }
});