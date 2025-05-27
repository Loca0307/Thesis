    // Event listeners for closing dialogs
    addDialogCloseListeners();

    // Event listeners for clicking outside dialogs to close
    addOutsideClickListeners();
}

// Handle season selection
function handleSeasonSelection(selectedSeason, homeSection, browseLoader, browseSection) {
    const racesKey = `races_${selectedSeason}`;
    const resultsKey = `results_${selectedSeason}`;
    const qualifyingKey = `qualifying_${selectedSeason}`;

    homeSection.style.display = "none";
    browseLoader.style.display = "block";
    browseSection.style.display = "none";

    let racesData = localStorage.getItem(racesKey);
    let qualifyingData = localStorage.getItem(qualifyingKey);
    let resultsData = localStorage.getItem(resultsKey);

    if (!(racesData && qualifyingData && resultsData)) {
        // Fetch and cache data if not already stored
        fetchSeasonData(selectedSeason).then((data) => {
            cacheSeasonData(racesKey, resultsKey, qualifyingKey, data);
            displayRaces(data[0], data[1], data[2], selectedSeason, browseLoader, browseSection);
        }).catch((error) => {
            console.error("Data fetch failed:", error);
            alert("Failed to fetch data. Please try again.");
            browseLoader.style.display = "none";
        });
    } else {
        // Use cached data
        racesData = JSON.parse(racesData);
        qualifyingData = JSON.parse(qualifyingData);
        resultsData = JSON.parse(resultsData);
        displayRaces(racesData, qualifyingData, resultsData, selectedSeason, browseLoader, browseSection);
    }
}

// Navigate back to home
function navigateToHome(homeSection, browseSection) {
    homeSection.style.display = "block";
    browseSection.style.display = "none";

    document.querySelector("#raceResults").style.display = "none";
    document.querySelector("#qualifying").innerHTML = "";
    document.querySelector("#results").innerHTML = "";
    document.querySelector("#seasonList").value = "";
}

// Populate season dropdown