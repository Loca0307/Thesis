const taskInput = document.getElementById("taskinput");

function addTask() {
  let task = taskInput.value.trim();
  if (task === "") return; // Prevent empty tasks

  alert("Task added!");

  const list = document.getElementById("tasklist");

  // Create Task Item Container
  let taskItem = document.createElement("div");
  taskItem.classList.add("task-item");

  // Create Task Description Div
  let taskTextContainer = document.createElement("div");
  taskTextContainer.textContent = task;
  taskTextContainer.classList.add("task-text-container");
  taskTextContainer.contentEditable = "false"; // Initially not editable

  // Create Buttons Container
  let buttonsContainer = document.createElement("div");
  buttonsContainer.classList.add("task-buttons");

  // Delete Button
  let deleteBtn = document.createElement("button");
  deleteBtn.textContent = "Delete";
  deleteBtn.classList.add("task-btn", "delete-btn");
  deleteBtn.onclick = function () {
      list.removeChild(taskItem);
  };

  // Complete Button
  let completeBtn = document.createElement("button");
  completeBtn.textContent = "Completed";
  completeBtn.classList.add("task-btn", "complete-btn");
  completeBtn.onclick = function () {
      taskTextContainer.style.textDecoration = "line-through";
      taskTextContainer.style.color = "gray";
  };

  // Edit Button
  let editBtn = document.createElement("button");
  editBtn.textContent = "Edit";
  editBtn.classList.add("task-btn", "edit-btn");
  editBtn.onclick = function () {
      if (taskTextContainer.contentEditable === "false") {
          taskTextContainer.contentEditable = "true";
          taskTextContainer.focus();
          editBtn.textContent = "Save";
      } else {
          taskTextContainer.contentEditable = "false";
          editBtn.textContent = "Edit";
      }
  };

  // Append Buttons to Buttons Container
  buttonsContainer.appendChild(editBtn);
  buttonsContainer.appendChild(completeBtn);
  buttonsContainer.appendChild(deleteBtn);

  // Append Task Description and Buttons to Task Item
  taskItem.appendChild(taskTextContainer);
  taskItem.appendChild(buttonsContainer);

  // Append Task Item to List
  list.appendChild(taskItem);

  // Clear Input
  taskInput.value = "";
}

// Attach event listener to "Add Task" button
document.querySelector("button").addEventListener("click", addTask);