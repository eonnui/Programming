const zenSound = new Audio('../audio/wind_chimes_1_16.wav');
        const zenPing = new Audio('../audio/click.wav');

        document.getElementById('pomodoro-timer').classList.add('active');
        const startButton = document.getElementById('start');
        const countdown = document.getElementById('timer');
        const resetButton = document.getElementById('reset');

        let selectedTime = "pomodoro-timer"
        let pomodoroCount = 0;
        let isRunning = false;
        let timeLeft;
        let interval;
        
        const timeMapping = {
                "short-break": 5 * 60,
                "long-break": 15 * 60,
                "pomodoro-timer": 25 * 60,
        };

        function playTrimmedSound(audio, startTime = 0, duration = 2){
            audio.currentTime = startTime;
            audio.play();

            setTimeout(() => {
                audio.pause();
                audio.currentTime = 0;
            }, duration * 1000)
        }

        function updateTimerDisplay(seconds) {
            const minutes = Math.floor(seconds / 60);
            const secs = seconds % 60;
            countdown.textContent = `${minutes}:${secs.toString().padStart(2, '0')}`
        };

        function toggleResetButton(show){
            resetButton.style.opacity = show ? 1 : 0;
        };

        function setActive(clickedButton){
            clearInterval(interval);
            startButton.textContent = "START";
            isRunning = false;
            playTrimmedSound(zenPing, 0, 2);

            document.querySelectorAll('button').forEach(button => {
                button.classList.remove('active');
            });
            clickedButton.classList.add('active');

            selectedTime = clickedButton.id;
            updateTimerDisplay(timeMapping[selectedTime]);
            timeLeft = timeMapping[selectedTime];
            toggleResetButton(false);
        };

        function startTimer(){
            if (isRunning) {
                clearInterval(interval);
                startButton.textContent = "START";
                playTrimmedSound(zenPing, 0, 2);
            } else {
                if (!timeLeft) timeLeft = timeMapping[selectedTime];
                interval = setInterval(() => {
                    timeLeft --;

                    updateTimerDisplay(timeLeft);

                    if (timeLeft <= 0) {
                        clearInterval(interval);
                        playTrimmedSound(zenSound, 76, 3);
                        isRunning = false;
                        handleCycle();
                    }

                }, 1000);
                startButton.textContent = "PAUSE";
                playTrimmedSound(zenPing, 0, 2);
            };

            isRunning = !isRunning;
            toggleResetButton(isRunning);
        };

        function resetTimer(){
            clearInterval(interval);
            isRunning = false;
            timeLeft = timeMapping[selectedTime];
            updateTimerDisplay(timeMapping[selectedTime]);
            updateTimerDisplay(timeLeft);
            startButton.textContent = "START";
            toggleResetButton(false);

            playTrimmedSound(zenPing, 0, 2);
        };

        function handleCycle() {
            if (selectedTime === "pomodoro-timer"){
                pomodoroCount++;
                console.log(`Pomodoros completed: ${pomodoroCount}`);

                if (pomodoroCount % 4 === 0) {
                    setActive(document.getElementById('long-break'));
                } else {
                    setActive(document.getElementById('short-break'));
                };
            } else {
                setActive(document.getElementById('pomodoro-timer'));
            }

            document.getElementById('year').textContent = new Date().getFullYear();
        };