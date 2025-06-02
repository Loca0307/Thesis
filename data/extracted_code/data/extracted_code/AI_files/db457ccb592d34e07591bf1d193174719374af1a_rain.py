# Step 1: Import Necessary Libraries
import tkinter as tk
import random
import time

# Step 2: Initialize Variables
window_size = 20
rain_rate = 0.1
drop_increase = 5
reset_size = 50

# Tkinter window and canvas size
canvas_size = 1000

# Step 3: Create a Tkinter Window and Canvas

# Initialize Tkinter window
root = tk.Tk()
root.title("Rain Simulation")

# Create canvas
canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="lightblue")
canvas.pack()

# Step 4: Create a Grid

# Draw grid lines
cell_size = canvas_size // window_size

for i in range(window_size + 1):
    # Vertical lines
    x = i * cell_size
    canvas.create_line(x, 0, x, canvas_size, fill="gray")
    # Horizontal lines
    y = i * cell_size
    canvas.create_line(0, y, canvas_size, y, fill="gray")


# Step 5: Represent Drops of Water

# Initialize drops of water with starting size
drops = [[0 for _ in range(window_size)] for _ in range(window_size)]

# Draw drops on the canvas
circles = [
    [
        canvas.create_oval(
            j * cell_size + cell_size // 4, i * cell_size + cell_size // 4,
            j * cell_size + 3 * cell_size // 4, i * cell_size + 3 * cell_size // 4,
            fill="blue"
        )
        for j in range(window_size)
    ]
    for i in range(window_size)
]

# Step 6: Simulate Rain

def update_drops():
    for i in range(window_size):
        for j in range(window_size):
            # Determine if this drop grows
            if random.random() < rain_rate:
                drops[i][j] += drop_increase
            
            # Check if the drop exceeds the reset size
            if drops[i][j] > reset_size:
                drops[i][j] = 0  # Reset the drop
                # Reset all drops below
                for k in range(i, window_size):
                    drops[k][j] = 0
            
            # Update the drop size on the canvas
            size = drops[i][j]
            canvas.coords(
                circles[i][j],
                j * cell_size + cell_size // 2 - size // 2,
                i * cell_size + cell_size // 2 - size // 2,
                j * cell_size + cell_size // 2 + size // 2,
                i * cell_size + cell_size // 2 + size // 2
            )

    # Schedule the next update
    root.after(50, update_drops)


# Step 7: Run the Simulation
update_drops()
root.mainloop()