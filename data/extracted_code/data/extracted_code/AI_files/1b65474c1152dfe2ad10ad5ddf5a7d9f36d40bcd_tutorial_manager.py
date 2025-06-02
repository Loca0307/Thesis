import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import webbrowser
import json
import subprocess
import requests
from bs4 import BeautifulSoup
import yt_dlp

# Data storage - Global Varieables
BG_COLOR = "#f5f5f5"
LABEL_FONT = ("Arial", 10)
HEADER_FONT = ("Arial", 11, "bold")
DATA_FILE = "tutorials.json"
tutorials = []
tags_set = set()
categories_set = set()
last_selected_index = None
current_tags_list = []  # holds tags added one-by-one from dropdown

# ----------------------- Tooltip Helper -----------------------
def add_tooltip(widget, text):
    def on_enter(e):
        tooltip = tk.Toplevel(widget)
        tooltip.wm_overrideredirect(True)
        tooltip.geometry(f"+{e.x_root+10}+{e.y_root+10}")
        label = tk.Label(tooltip, text=text, background="#ffffe0", relief="solid", borderwidth=1, font=("Arial", 8))
        label.pack()
        widget.tooltip = tooltip
    def on_leave(e):
        if hasattr(widget, "tooltip"):
            widget.tooltip.destroy()
    widget.bind("<Enter>", on_enter)
    widget.bind("<Leave>", on_leave)

# ----------------------- Persistence -----------------------
def load_data():
    global tutorials, tags_set, categories_set
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            tutorials = json.load(f)
            tags_set = set()
            categories_set = set()
            for tut in tutorials:
                tags_set.update(tut.get("tags", []))
                categories_set.add(tut.get("category", ""))

def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(tutorials, f, indent=4)

# ----------------------- Utility -----------------------
def update_dropdowns():
    cat_combo['values'] = sorted(categories_set)
    tag_combo['values'] = sorted(tags_set)

def update_listbox():
    tutorial_listbox.delete(0, tk.END)
    for i, tut in enumerate(tutorials):
        tag_display = ", ".join(tut.get("tags", []))
        tutorial_listbox.insert(tk.END, f"{tut['title']} [{tut['category']}] ({tag_display})")

# ----------------------- Add/Edit/Delete -----------------------
def add_tutorial():
    title = title_var.get().strip()
    category = category_var.get().strip()
    path = path_var.get().strip()
    tags = current_tags_list.copy()

    if not title or not category or not path:
        messagebox.showerror("Error", "Please fill in all required fields.")
        return

    categories_set.add(category)
    tags_set.update(tags)

    tutorials.append({
        "title": title,
        "category": category,
        "path": path,
        "type": "local" if os.path.exists(path) else "youtube",
        "tags": tags
    })
    update_listbox()
    update_dropdowns()
    save_data()

    title_var.set("")
    category_var.set("")
    path_var.set("")
    tag_var.set("")
    
    # ✅ Clear selected tags list visually and in memory
    current_tags_list.clear()
    tag_listbox.delete(0, tk.END)

def edit_selected():
    index = get_selected_index()
    if index is None:
        return

    # Log current values (for debugging)
    print("Editing index:", index)
    print("Before:", tutorials[index])

    title = title_var.get().strip()
    category = category_var.get().strip()
    path = path_var.get().strip()
    tags = list(tag_listbox.get(0, tk.END))  # get only the tags currently shown


    if not title or not category or not path:
        messagebox.showerror("Error", "Please fill in all required fields.")
        return

    tutorials[index] = {
        "title": title,
        "category": category,
        "path": path,
        "type": "local" if os.path.exists(path) else "youtube",
        "tags": tags
    }

    save_data()
    update_listbox()
    update_dropdowns()
    title_var.set("")
    category_var.set("")
    path_var.set("")
    tag_var.set("")
    
    # ✅ Clear selected tags list visually and in memory
    current_tags_list.clear()
    tag_listbox.delete(0, tk.END)

    print("After:", tutorials[index])
    messagebox.showinfo("Edit Successful", f"Tutorial \"{title}\" was updated.")

def delete_selected():
    index = get_selected_index()
    if index is None:
        return
    if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this tutorial?"):
        tutorials.pop(index)
        update_listbox()
        save_data()

# ----------------------- Helper -----------------------
def get_selected_index():
    selected = tutorial_listbox.curselection()
    if selected:
        return selected[0]
    if last_selected_index is not None:
        return last_selected_index
    messagebox.showinfo("Select Tutorial", "Please select a tutorial.")
    return None

def on_listbox_select(event):
    global last_selected_index
    selected = tutorial_listbox.curselection()
    if not selected:
        return  # Exit early if no selection

    last_selected_index = selected[0]
    tut = tutorials[last_selected_index]
    title_var.set(tut['title'])
    category_var.set(tut['category'])
    path_var.set(tut['path'])
    tag_var.set(", ".join(tut.get("tags", [])))

    current_tags_list.clear()
    tag_listbox.delete(0, tk.END)

    for tag in tut.get("tags", []):
        current_tags_list.append(tag)
        tag_listbox.insert(tk.END, tag)

def browse_file():
    path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.mov *.avi *.mkv")])
    if path:
        path_var.set(path)

def preview_selected():
    index = get_selected_index()
    if index is None:
        return
    path = tutorials[index]['path']
    video_title_label.config(text=f"Now Playing: {tutorials[index]['title']}")
    if tutorials[index]['type'] == 'youtube':
        webbrowser.open(path)
    else:
        try:
            subprocess.Popen(['start', '', path], shell=True)
        except Exception as e:
            messagebox.showerror("Error", f"Could not open video: {e}")

# ----------------------- Add Tag/Category -----------------------
def add_tag():
    new_tags = tag_var.get().strip()
    if new_tags:
        for tag in new_tags.split(','):
            tag = tag.strip()
            if tag:
                tags_set.add(tag)
        update_dropdowns()
        tag_var.set("")

def add_category():
    new_cat = category_var.get().strip()
    if new_cat:
        categories_set.add(new_cat)
        update_dropdowns()
        category_var.set("")
        
def add_tag_to_list():
    tag = tag_var.get().strip()
    if tag and tag not in current_tags_list:
        current_tags_list.append(tag)
        tag_listbox.insert(tk.END, tag)
        tag_var.set("")

def remove_selected_tag():
    selected = tag_listbox.curselection()
    if selected:
        index = selected[0]
        current_tags_list.pop(index)
        tag_listbox.delete(index)


# ----------------------- Search -----------------------
def search_tutorials():
    keyword = search_var.get().strip().lower()
    filter_by = search_by_var.get()
    tutorial_listbox.delete(0, tk.END)
    for tut in tutorials:
        if filter_by == "Title" and keyword in tut['title'].lower():
            insert_filtered(tut)
        elif filter_by == "Category" and keyword in tut['category'].lower():
            insert_filtered(tut)
        elif filter_by == "Tag" and any(keyword in t.lower() for t in tut.get('tags', [])):
            insert_filtered(tut)

def insert_filtered(tut):
    tag_display = ", ".join(tut.get("tags", []))
    tutorial_listbox.insert(tk.END, f"{tut['title']} [{tut['category']}] ({tag_display})")

# ----------------------- URL Metadata Fetch -----------------------

def fetch_info_from_url():
    url = path_var.get().strip()
    if not url:
        messagebox.showwarning("No URL", "Please enter a URL or path first.")
        return

    # YouTube/Vimeo via yt_dlp
    if "youtube.com" in url or "youtu.be" in url or "vimeo.com" in url:
        try:
            ydl_opts = {'quiet': True, 'skip_download': True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                title_var.set(info.get("title", ""))
                messagebox.showinfo("Success", "Fetched info from video successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch video info: {e}")
    else:
        # Try generic page title
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.title.string.strip() if soup.title else ""
            title_var.set(title)
            messagebox.showinfo("Success", "Fetched page title successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch webpage info: {e}")
            
# ----------------------- Rest for Function -----------------------
def clear_form(event=None):
    global last_selected_index
    last_selected_index = None
    title_var.set("")
    category_var.set("")
    path_var.set("")
    tag_var.set("")
    current_tags_list.clear()
    tag_listbox.delete(0, tk.END)


# ----------------------- UI -----------------------
root = tk.Tk()
root.configure(bg=BG_COLOR)
root.title("🎓 Tutorial Manager")
root.geometry("800x600")

# --- Input Frame ---
input_frame = tk.LabelFrame(root, text="🛠️ Add / Edit Tutorial", padx=10, pady=10, font=HEADER_FONT, bg=BG_COLOR)
input_frame.pack(fill="x", padx=10, pady=5)

title_var = tk.StringVar()
category_var = tk.StringVar()
path_var = tk.StringVar()
tag_var = tk.StringVar()

# Title
tk.Label(input_frame, text="Title:").grid(row=0, column=0, sticky="e")
title_entry = tk.Entry(input_frame, textvariable=title_var, width=30)
title_entry.grid(row=0, column=1, padx=5)

# Category with dropdown
tk.Label(input_frame, text="Category:").grid(row=1, column=0, sticky="e")
cat_combo = ttk.Combobox(input_frame, textvariable=category_var, width=28)
cat_combo.grid(row=1, column=1, padx=5)
tk.Button(input_frame, text="+", width=2, command=add_category).grid(row=1, column=2)

# Tags with dropdown
tk.Label(input_frame, text="Tags (comma-separated):").grid(row=2, column=0, sticky="e")
tag_combo = ttk.Combobox(input_frame, textvariable=tag_var, width=28)
tag_combo.grid(row=2, column=1, padx=5)
add_tooltip(tag_combo, "Type or select a tag. Use commas for multiple.")
tk.Button(input_frame, text="+", width=2, command=add_tag).grid(row=2, column=2)
add_tag_button = tk.Button(input_frame, text="Add Tag to List", command=add_tag_to_list)
add_tag_button.grid(row=2, column=3, padx=5)
add_tooltip(add_tag_button, "Click to add the selected tag to the list below.")

# Tag Listbox to display added tags
tk.Label(input_frame, text="Selected Tags:").grid(row=5, column=0, sticky="ne")
tag_listbox = tk.Listbox(input_frame, height=4)
add_tooltip(tag_listbox, "These are the tags currently added to this tutorial.")
tag_listbox.grid(row=5, column=1, columnspan=2, sticky="we")
remove_tag_button = tk.Button(input_frame, text="Remove Selected Tag", command=remove_selected_tag)
remove_tag_button.grid(row=5, column=3)
add_tooltip(remove_tag_button, "Removes the selected tag from the list.")

# Path
tk.Label(input_frame, text="Path or URL:").grid(row=3, column=0, sticky="e")
path_entry = tk.Entry(input_frame, textvariable=path_var, width=30)
path_entry.grid(row=3, column=1, padx=5, sticky="w")
browse_button = tk.Button(input_frame, text="📂", command=browse_file)
browse_button.grid(row=3, column=2)
fetch_info_button = tk.Button(input_frame, text="🔍 Fetch Info", command=fetch_info_from_url)
fetch_info_button.grid(row=3, column=3)
add_tooltip(fetch_info_button, "Fetch the title from a YouTube/Vimeo or website URL.")

# Buttons
add_button = tk.Button(input_frame, text="➕ Add", width=10, command=add_tutorial)
add_button.grid(row=4, column=0, pady=5)

edit_button = tk.Button(input_frame, text="✏️ Edit", width=10, command=edit_selected)
edit_button.grid(row=4, column=1, pady=5)

delete_button = tk.Button(input_frame, text="❌ Delete", width=10, command=delete_selected)
delete_button.grid(row=4, column=2, pady=5)

# --- Search Frame ---
search_frame = tk.Frame(root)
search_frame.pack(fill="x", padx=10, pady=5)

search_var = tk.StringVar()
search_by_var = tk.StringVar(value="Title")
search_entry = tk.Entry(search_frame, textvariable=search_var, width=30)
search_entry.pack(side="left", padx=5)

tk.OptionMenu(search_frame, search_by_var, "Title", "Category", "Tag").pack(side="left")
search_frame = tk.LabelFrame(root, text="🔍 Search Tutorials", font=HEADER_FONT, padx=10, pady=5, bg=BG_COLOR)

# --- Tutorial List ---
list_frame = tk.LabelFrame(root, text="📚 Tutorials", font=HEADER_FONT, bg=BG_COLOR)
list_frame.pack(fill="both", expand=True, padx=10, pady=5)

tutorial_listbox = tk.Listbox(list_frame, height=12)
tutorial_listbox.pack(side="left", fill="both", expand=True)
tutorial_listbox.bind("<<ListboxSelect>>", on_listbox_select)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")
tutorial_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tutorial_listbox.yview)

# --- Preview ---
preview_frame = tk.Frame(root)
preview_frame.pack(fill="x", padx=10)
tk.Button(preview_frame, text="▶ Preview", width=25, command=preview_selected).pack(pady=5)
video_title_label = tk.Label(preview_frame, text="Now Playing: None", font=("Arial", 10, "italic"))
video_title_label.pack()

add_tooltip(add_button, "Save a new tutorial using the form above.")
add_tooltip(edit_button, "Apply changes to the selected tutorial.")
add_tooltip(delete_button, "Remove the selected tutorial permanently.")
add_tooltip(search_entry, "Search tutorials by title, category, or tag.")


# Run
load_data()
update_listbox()
update_dropdowns()

def is_click_outside_widgets(event):
    widget = root.winfo_containing(event.x_root, event.y_root)
    allowed_widgets = [
        tutorial_listbox, search_entry,
        title_entry, cat_combo, tag_combo,
        path_entry, tag_listbox,
        add_button, edit_button, delete_button,
        browse_button, fetch_info_button,
        add_tag_button, remove_tag_button
    ]
    if widget not in allowed_widgets:
        clear_form()
        
root.bind("<Button-1>", is_click_outside_widgets)
root.mainloop()