const formChrono = document.querySelector("form");
const inputChrono = document.querySelector("input");
const renderChrono = document.querySelector("h2");

formChrono.addEventListener("submit", (e) => {
  e.preventDefault();
  inputChrono.value = "";
  if (inputChrono.value <= 0) {
      return alert("Veuillez utiliser minimum le chiffre 1 !");
    }
    playChrono(inputChrono.value);
});

function playChrono(value) {
  let minutes = parseInt(value);
  let seconds = 0;

  const intervalId = setInterval(() => {
    if (minutes === 0 && seconds === 0) {
      clearInterval(intervalId);
      return alert("finish !");
    } else if (seconds === 0) {
      minutes -= 1;
      seconds = 59;
    } else {
      seconds -= 1;
    }

    renderChrono.textContent = `${minutes} : ${
      seconds < 10 ? "0" + seconds : seconds
    }`;
  }, 1000);
}