    continueButton3.addEventListener("click", function() {
      if(checkNumbers() && stage === 3) {
        userData = [];
        step3Container.querySelectorAll(".skill").forEach(skill => {
          currentInput = skill.querySelector(".skillsInput")
          if (!currentInput.disabled) {
            userData.push(currentInput.value);
          }
        });
        stage = 4; // Change to results stage
        staggerButtonsReverse(skillGrid, 200);
        staggerButtonsReverse(document.querySelectorAll(".skillLabel"), 250);
        continueButton3.style.cssText = "opacity: 0; transform: translateY(-20);";
        setTimeout(function() {
          continueButton3.style.cssText = "opacity: 0; display: none;";
          document.getElementById("parent-container").style.display = "none";
        }, 2000);



        const sum = userData.reduce((accumulator, currentValue) => accumulator + parseInt(currentValue, 10), 0);
        const totalPoints = (positionSkills[userPosition].length) * 10 // Take the number of skills * 10(max points)
        const percentage = Math.round((sum/totalPoints)*100) // Round to nearest whole number for ranking
        //console.log(percentage + " therefore rank: "+ getRank(percentage));
        var config = {
          type: 'radar',
          data: {
            labels: positionSkills[userPosition],
            datasets: [{
              label: "Skill Results",
              backgroundColor: "rgba(69, 162, 158, 0.6)",
              borderColor: "white",
              pointBackgroundColor: "white",
              pointRadius: 5.3,
              data: userData,
            }]
          },
          options: {
            legend: {
              position: 'top',
              labels: {
                fontColor: 'white'
              }
            },
            scale: {
              ticks: {
                beginAtZero: true,
                fontColor: 'white', // labels such as 10, 20, etc
                showLabelBackdrop: false, // hide square behind text
                suggestedMax: 10,
                callback: function(value) {
                  // Show only '10' 5 and 1, hide other values
                  return value === 10 || value === 5 || value === 1? value : '';
              }
              },
              pointLabels: {
                fontColor: '#c5c6c7',
                fontSize: 18,
              },
              gridLines: {
                color: 'grey'
              },
              angleLines: {
                color: 'white' // lines radiating from the center
              }
            },
          }
        };
        const drawChart = new Chart(skillChart, config);
        step4Container.style.display = "block";
        setTimeout(function() {
          document.getElementById("chartContainer").style.left = "85%"
          document.getElementById("continueButton4").style.cssText = "transform: translateY(0); opacity: 1;";
        }, 2000);
      } 
})
