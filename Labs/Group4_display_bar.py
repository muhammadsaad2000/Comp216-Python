import tkinter as tk
from tkinter import ttk, Entry, Canvas

class WeatherDisplayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Display App")

        # Default values
        self.temperature = 25.0
        self.temperature_units = "°C"

        # Style configuration
        style = ttk.Style()
        style.configure("TFrame", background="#ecf0f1")
        style.configure("TButton", background="#3498db", foreground="white", padding=(10, 5), font=('Helvetica', 12, 'bold'))
        style.configure("TEntry", padding=(10, 5), font=('Helvetica', 12))

        # Create and configure the notebook (tabs)
        self.notebook = ttk.Notebook(root, style="TFrame")
        self.notebook.grid(row=0, column=0, columnspan=2, pady=10, padx=20, sticky="nsew")

        # Add the temperature tab
        self.create_tab("Temperature", self.temperature, self.temperature_units)

    def create_tab(self, parameter, value, units):
        tab_frame = ttk.Frame(self.notebook, style="TFrame")
        tab_frame.grid(row=0, column=0, pady=10)

        # Create and configure the display for the parameter
        canvas = Canvas(tab_frame, width=150, height=200, bg="white", highlightbackground="#3498db", highlightthickness=1)
        canvas.grid(row=0, column=0, columnspan=2, pady=10)
        self.update_display(canvas, value, units)

        # Entry for changing the parameter value
        entry = Entry(tab_frame, font=('Helvetica', 12), justify="center", width=10)
        entry.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        # Button to update the parameter value
        update_button = ttk.Button(tab_frame, text="Update", command=lambda p=parameter, e=entry: self.update_parameter(parameter, entry))
        update_button.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        # Add the tab to the notebook
        self.notebook.add(tab_frame, text=parameter)

    def update_display(self, canvas, value, units):
        # Clear previous display
        canvas.delete("all")

        # Draw the parameter indicator
        indicator_height = self.calculate_indicator_height(value)
        canvas.create_rectangle(30, 40 + 150 - indicator_height, 40, 20 + 150,
                                fill="#3498db", outline="#2c3e50")

        # Display the parameter value
        canvas.create_text(50, 180, text=f"{value} {units}", font=("Helvetica", 12, "bold"))

    def calculate_indicator_height(self, value):
        return int((value - 0) / (100 - 0) * 150)  # Adjust range if needed

    def update_parameter(self, parameter, entry):
        try:
            # Get the new parameter value from the entry
            new_value = float(entry.get())

            # Check if the new value is within the valid range
            if parameter == "Temperature" and not (-50 <= new_value <= 100):
                print(f"{parameter} value must be between -50 and 100.")
                return

            if -50 <= new_value <= 100:
                setattr(self, parameter.lower(), new_value)
                tab_index = ["Temperature"].index(parameter)
                canvas = self.notebook.winfo_children()[tab_index].winfo_children()[0]
                self.update_display(canvas, new_value, getattr(self, f"{parameter.lower()}_units"))
            else:
                print(f"{parameter} value must be between -50 and 50.")
        except ValueError:
            print(f"Invalid {parameter} value.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherDisplayApp(root)
    
    # Set uniform weight for notebook rows and columns
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()
