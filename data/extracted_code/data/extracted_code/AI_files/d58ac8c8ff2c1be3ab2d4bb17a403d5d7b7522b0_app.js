async function fetchData() {
    try {
        const response = await fetch('https://swapi.dev/api/people/');
        const data = await response.json();
        createTable(data.results);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

function createTable(data) {
    const table = document.createElement('table');
    const headerRow = document.createElement('tr');

    // Create table headers
    const headers = ['Name', 'Height', 'Mass', 'Hair Color', 'Skin Color', 'Eye Color', 'Birth Year', 'Gender'];
    headers.forEach(headerText => {
        const header = document.createElement('th');
        header.textContent = headerText;
        headerRow.appendChild(header);
    });
    table.appendChild(headerRow);

    // Create table rows
    data.forEach(item => {
        const row = document.createElement('tr');
        Object.values(item).slice(0, 8).forEach(text => {
            const cell = document.createElement('td');
            cell.textContent = text;
            row.appendChild(cell);
        });
        table.appendChild(row);
    });

    // Append table to the div
    const dataTable = document.getElementById('data-table');
    dataTable.innerHTML = ''; // Clear any existing content
    dataTable.appendChild(table);
}