import tkinter as tk
import json

def load_data():
    # Load data from the JSON file
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"column1": [], "column2": []}

    return data

def save_data(data):
    # Save data to the JSON file
    with open("data.json", "w") as file:
        json.dump(data, file)

def add_text():
    text = text_entry.get()

    if selected_column.get() == "Column 1":
        data["column1"].append(text)
    elif selected_column.get() == "Column 2":
        data["column2"].append(text)

    save_data(data)
    refresh_lists()

def refresh_lists():
    # Clear the existing lists
    listbox1.delete(0, tk.END)
    listbox2.delete(0, tk.END)

    # Add items from the data to the lists
    for item in data["column1"]:
        listbox1.insert(tk.END, item)

    for item in data["column2"]:
        listbox2.insert(tk.END, item)

# Load initial data from the JSON file
data = load_data()

# Create the main window
root = tk.Tk()

# Create a label and pack it
label = tk.Label(root, text="Enter Text:")
label.pack()

# Create a text entry widget
text_entry = tk.Entry(root)
text_entry.pack()

# Create a radio button to select the column
selected_column = tk.StringVar(value="Column 1")
column1_radio = tk.Radiobutton(root, text="Column 1", variable=selected_column, value="Column 1")
column1_radio.pack(anchor=tk.W)
column2_radio = tk.Radiobutton(root, text="Column 2", variable=selected_column, value="Column 2")
column2_radio.pack(anchor=tk.W)

# Create a button to add text to the selected column
button = tk.Button(root, text="Add Text", command=add_text)
button.pack()

# Create a frame to hold the listboxes
frame = tk.Frame(root)
frame.pack(side=tk.LEFT)

# Create a listbox for Column 1
listbox1 = tk.Listbox(frame)
listbox1.pack(side=tk.LEFT)

# Create a listbox for Column 2
listbox2 = tk.Listbox(frame)
listbox2.pack(side=tk.LEFT)

# Refresh the lists initially
refresh_lists()

# Run the main event loop
root.mainloop()