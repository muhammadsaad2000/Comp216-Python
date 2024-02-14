import tkinter as tk
from tkinter import ttk, messagebox

class SimpleApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple GUI Application")
        self.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        self.frame = ttk.Frame(self, padding="10", relief="ridge", width=300)
        self.frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.create_labels()
        self.create_entries()
        self.create_radiobuttons()
        self.create_combobox()
        self.create_checkbuttons()
        self.create_buttons()

        self.reset_form()
        self.configure_resizing()

    def create_labels(self):
        ttk.Label(self.frame, text="Data Entry Form", font=('Helvetica', 16)).grid(row=0, column=0, columnspan=2, pady=(0, 10))
        ttk.Label(self.frame, text="Full Name:").grid(row=1, column=0, sticky="w")
        ttk.Label(self.frame, text="Residency:").grid(row=2, column=0, sticky="w")
        ttk.Label(self.frame, text="Program:").grid(row=3, column=0, sticky="w")
        ttk.Label(self.frame, text="Courses:").grid(row=4, column=0, sticky="w")

    def create_entries(self):
        self.username_entry = ttk.Entry(self.frame)
        self.username_entry.grid(row=1, column=1, sticky="ew")

    def create_radiobuttons(self):
        self.residency_var = tk.StringVar()
        ttk.Radiobutton(self.frame, text="Domestic", variable=self.residency_var, value="dom").grid(row=2, column=1, sticky="w")
        ttk.Radiobutton(self.frame, text="International", variable=self.residency_var, value="intl").grid(row=2, column=1, sticky="e")

    def create_combobox(self):
        self.program_var = tk.StringVar()
        program_combobox = ttk.Combobox(self.frame, textvariable=self.program_var, values=["AI", "Gaming", "Health", "Software"])
        program_combobox.grid(row=3, column=1, sticky="ew")
        program_combobox.set("AI")

    def create_checkbuttons(self):
        self.comp100_var = tk.StringVar(value="")
        ttk.Checkbutton(self.frame, text="Programming I", variable=self.comp100_var, onvalue="COMP100").grid(row=4, column=1, sticky="w")

        self.comp213_var = tk.StringVar(value="")
        ttk.Checkbutton(self.frame, text="Web Page Design", variable=self.comp213_var, onvalue="COMP213").grid(row=5, column=1, sticky="w")

        self.comp120_var = tk.StringVar(value="")
        ttk.Checkbutton(self.frame, text="Software Engineering", variable=self.comp120_var, onvalue="COMP120").grid(row=6, column=1, sticky="w")

    def create_buttons(self):
        ttk.Button(self.frame, text="Reset", command=self.reset_form).grid(row=7, column=0, pady=(10, 0), sticky="ew")
        ttk.Button(self.frame, text="Ok", command=self.show_info).grid(row=7, column=1, pady=(10, 0), sticky="ew")
        ttk.Button(self, text="Exit", command=self.destroy).grid(row=1, column=0, pady=10)

    def reset_form(self):
        self.username_entry.delete(0, tk.END)
        self.residency_var.set("dom")
        self.program_var.set("AI")
        self.comp100_var.set("")
        self.comp213_var.set("")
        self.comp120_var.set("")

    def show_info(self):
        info_message = f"Full Name: {self.username_entry.get()}\nResidency: {self.residency_var.get()}\n" \
                       f"Program: {self.program_var.get()}\nCourses: {', '.join(filter(None, [self.comp100_var.get(), self.comp213_var.get(), self.comp120_var.get()]))}"

        messagebox.showinfo("Information", info_message)

    def configure_resizing(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

if __name__ == "__main__":
    app = SimpleApp()
    app.mainloop()
