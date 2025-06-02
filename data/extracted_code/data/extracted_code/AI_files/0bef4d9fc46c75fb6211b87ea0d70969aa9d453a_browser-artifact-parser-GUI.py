        self.status_text = tk.Text(root, height=20, width=70, state="disabled", bg="black", fg="white")
        self.status_text.grid(row=3, column=1, columnspan=2, padx=20, pady=20)

        tk.Button(root, text="Exit", width=10, command=self.exit, bg="red").grid(row=2, column=2, padx=10, pady=5)

    def exit(self):
        exit()
