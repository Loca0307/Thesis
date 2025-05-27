
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dice Roller</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Dice Roller</h1>
        <div class="dice" id="dice"></div>
        <button onclick="rollDice()">Roll</button>
        <button onclick="saveResult()">Save</button>
        <button onclick="resetResults()">Reset</button>
        <div class="results">
            <h2>Saved Results:</h2>
            <ul id="savedResults"></ul>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>


<!-- OLD CODE -->

<!-- <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dice Roller</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Dice Roller</h1>
        <div class="dice" id="dice">1</div>
        <button onclick="rollDice()">Roll</button>
        <button onclick="saveResult()">Save</button>
        <button onclick="resetResults()">Reset</button>
        <div class="results">
            <h2>Saved Results:</h2>
            <ul id="savedResults"></ul>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html> -->