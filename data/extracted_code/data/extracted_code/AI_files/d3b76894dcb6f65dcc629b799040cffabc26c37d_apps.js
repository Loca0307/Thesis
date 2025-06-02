  const resultsContainer = document.getElementById('report');
  resultsContainer.innerHTML = ''; // Clear previous results

  // Loop through allPictures and display results
  state.allPictures.forEach((picture) => {
    const resultItem = document.createElement('p');
    resultItem.textContent = `${picture.name}: Votes - ${picture.votes}, Seen - ${picture.views}`;
    resultsContainer.appendChild(resultItem);
  });
