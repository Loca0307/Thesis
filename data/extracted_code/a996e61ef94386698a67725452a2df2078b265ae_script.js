<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task Manager</title>
    <link rel="stylesheet" href="styles.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Sortable/1.14.0/Sortable.min.js"></script>
</head>
<body>
    <div class="container">
        <h1>Task Manager</h1>
        <div class="add-task-form">
            <input type="text" id="task-desc" placeholder="Enter task description">
            <label for="static-priority">Static Priority:</label>
            <select id="static-priority">
                <option value="1">1 - Critical</option>
                <option value="2">2 - Urgent</option>
                <option value="3">3 - Important but not urgent</option>
                <option value="4">4 - Low priority</option>
                <option value="5">5 - Very low priority</option>
            </select>
            
            <label for="daily-priority">Daily Priority:</label>
            <select id="daily-priority">
                <option value="1">1 - Critical</option>
                <option value="2">2 - Urgent</option>
                <option value="3">3 - Important but not urgent</option>
                <option value="4">4 - Low priority</option>
                <option value="5">5 - Very low priority</option>
            </select>
        
            <button id="add-task-btn">Add Task</button>
        </div>
    <script src="script.js"></script>
</body>
</html>