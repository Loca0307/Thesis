
// Create function to create new palette board

let newButton = document.querySelector('.new-button');
newButton.addEventListener('click', () => {
  localStorage.setItem(`currentName`, ``);
  localStorage.setItem(`currentColor1`, `null`);
  localStorage.setItem(`currentColor2`, `null`);
  localStorage.setItem(`currentColor3`, `null`);
  localStorage.setItem(`currentColor4`, `null`);
  localStorage.setItem(`currentColor5`, `null`);
  localStorage.setItem(`currentColor6`, `null`);
  localStorage.setItem(`currentColor7`, `null`);
  currentColor1 = localStorage.getItem('currentColor1');
  currentColor2 = localStorage.getItem('currentColor2');
  currentColor3 = localStorage.getItem('currentColor3');
  currentColor4 = localStorage.getItem('currentColor4');
  currentColor5 = localStorage.getItem('currentColor5');
  currentColor6 = localStorage.getItem('currentColor6');
  currentColor7 = localStorage.getItem('currentColor7');
  for(let i = 1; i < 8; i++) {
    console.log(localStorage.getItem(`currentColor${i}`));
    if ((localStorage.getItem(`currentColor${i}`)) === 'null') {
      document.querySelector(`.column${i} label`).style.backgroundColor = 'lightgray';
      for(let j = 1; j < 10; j++) {
        document.querySelector(`.column${i} .shade${j}`).style.backgroundColor = 'lightgray';
        document.querySelector(`.column${i} .shade${j}`).textContent = null;
      }
      continue;
    } else {
      console.log('working');
      let hue = hexToHue(localStorage.getItem(`currentColor${i}`));
      shadeHue(hue, `${i}`);
      applyTrueColor((localStorage.getItem(`currentColor${i}`)), `${i}`);
    }
  }
  nameBox.value = null;
  while(savedNameBox.firstChild) {
    savedNameBox.removeChild(savedNameBox.firstChild);
  };
  savedNameBox.style.zIndex = 0;
})