<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tumblr Blog Viewer</title>
    <link rel="stylesheet" href="styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
</head>
<body>
    <header>
        <h1><span class="material-icons">rss_feed</span> Tumblr Blog Viewer</h1>
        <button id="theme-toggle" class="button"><span class="material-icons">dark_mode</span></button>
        <button id="admin-toggle" class="button"><span class="material-icons">settings</span></button>
    </header>

    <div class="controls">
        <input type="text" id="search-input" placeholder="Search posts...">
        <select id="filter-select">
            <option value="all">All Posts</option>
            <option value="text">Text</option>
            <option value="photo">Photo</option>
            <option value="video">Video</option>
        </select>
    </div>

    <main id="posts-container"></main>

    <div class="pagination">
        <button id="prev-page" class="button" disabled>Previous</button>
        <span id="page-info">Page 1</span>
        <button id="next-page" class="button">Next</button>
    </div>

    <footer>
        <div class="social-links" id="social-links"></div>
        <div class="donation-links" id="donation-links">
            <h3>Support Us</h3>
        </div>
    </footer>

    <div id="admin-panel" class="hidden">
        <h2>Edit Links</h2>
        <div id="social-edit">
            <h3>Social Media Links</h3>
            <input type="text" id="twitter" placeholder="Twitter URL">
            <input type="text" id="facebook" placeholder="Facebook URL">
            <input type="text" id="instagram" placeholder="Instagram URL">
            <input type="text" id="tumblr" placeholder="Tumblr URL">
        </div>

        <div id="donation-edit">
            <h3>Donation Links</h3>
            <input type="text" id="venmo" placeholder="Venmo URL">
            <input type="text" id="paypal" placeholder="PayPal URL">
            <input type="text" id="cashapp" placeholder="Cash App URL">
            <input type="text" id="crypto" placeholder="Crypto URL">
        </div>

        <button id="save-links">Save</button>
    </div>

    <script src="script.js"></script>
</body>
</html>