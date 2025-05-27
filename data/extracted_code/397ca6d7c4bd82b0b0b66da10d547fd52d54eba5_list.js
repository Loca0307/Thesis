
    const searchInput = document.getElementById('teamSearchInput');
    const tableRows = document.querySelectorAll('tbody tr');
    
    searchInput.addEventListener('input', function() {
        const searchTerm = searchInput.value.trim();
        
        tableRows.forEach(row => {
            const teamNumberCell = row.querySelector('td:first-child');
            if (teamNumberCell) {
                const teamNumberText = teamNumberCell.textContent.trim();
                
                // Show/hide the row based on whether the team number contains the search term
                row.style.display = searchTerm === '' || teamNumberText.includes(searchTerm) ? '' : 'none';
            }
        });
    });