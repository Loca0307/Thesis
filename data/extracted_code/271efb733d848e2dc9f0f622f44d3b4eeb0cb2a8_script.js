document.getElementById('nav-list').addEventListener('click', function(event) {
    if (event.target.tagName === 'A') {
        alert('You clicked on ' + event.target.textContent);
    }
});