import tkinter as tk
import random

class NumberTableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Szám táblázat")
        
        self.rows = 5
        self.cols = 4
        self.table = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        
        self.buttons = []
        for col in range(self.cols):
            btn = tk.Button(root, text=f"Oszlop {col+1}", command=lambda c=col: self.add_number_to_column(c))
            btn.grid(row=0, column=col)
            self.buttons.append(btn)
        
        self.cells = [[tk.Label(root, text="", width=10, height=2, relief="ridge", borderwidth=2) 
                       for _ in range(self.cols)] for _ in range(self.rows)]
        
        for r in range(self.rows):
            for c in range(self.cols):
                self.cells[r][c].grid(row=r+1, column=c)
        
        self.number_var = tk.StringVar(value=str(random.choice([2, 4, 8, 16, 32, 64])))
        tk.Label(root, text="Következő szám:").grid(row=self.rows+1, column=0, columnspan=2)
        self.number_entry = tk.Entry(root, textvariable=self.number_var, font=("Arial", 14))
        self.number_entry.grid(row=self.rows+1, column=2, columnspan=2)
    
    def add_number_to_column(self, col):
        new_number = int(self.number_var.get())
        last_empty = None
        
        for row in range(self.rows):  # Fentről lefelé keres
            if self.table[row][col] is None:
                last_empty = row
                break
            
        if last_empty is not None:
            self.table[last_empty][col] = new_number
        else:
            return  # Ha tele van az oszlop, nem csinál semmit
        
        for row in range(self.rows - 1, 0, -1):  # Ellenőrzi az összevonást
            if self.table[row][col] is not None and self.table[row][col] == self.table[row - 1][col]:
                self.table[row - 1][col] *= 2
                self.table[row][col] = None
                last_empty = row
        
        self.update_display()
        self.generate_new_number()
    
    def update_display(self):
        for r in range(self.rows):
            for c in range(self.cols):
                self.cells[r][c].config(text=str(self.table[r][c]) if self.table[r][c] is not None else "")
    
    def generate_new_number(self):
        self.number_var.set(str(random.choice([2, 4, 8, 16, 32, 64])))

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberTableApp(root)
    root.mainloop()