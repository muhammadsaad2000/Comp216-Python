import tkinter as tk
from tkinter import Entry, Button

class TemperatureDisplayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Display App")

        # Default temperature value
        self.temperature = 25.0  # You can set your initial value here

        # Additional information for credibility
        self.units = "°C"
        self.low_value = 10.0
        self.normal_range = (18.0, 25.0)
        self.high_value = 100.0

        # Create and configure the thermometer display
        self.canvas = tk.Canvas(root, width=40, height=200, bg="white")
        self.canvas.grid(row=0, column=0, columnspan=2, pady=10)
        self.update_thermometer()

        # Entry for changing the temperature value
        self.entry = Entry(root)
        self.entry.grid(row=1, column=0, padx=10)

        # Button to update the temperature value
        self.update_button = Button(root, text="Update", command=self.update_temperature)
        self.update_button.grid(row=1, column=1, padx=10)

    def update_thermometer(self):
        # Clear previous thermometer display
        self.canvas.delete("all")

        # Draw the thermometer shape
        thermometer_x = 20
        thermometer_y = 20
        thermometer_width = 20
        thermometer_height = 150

        self.canvas.create_rectangle(thermometer_x, thermometer_y,
                                     thermometer_x + thermometer_width, thermometer_y + thermometer_height,
                                     fill="lightgray", outline="black")

        # Calculate the temperature indicator height
        value_percent = (self.temperature - self.low_value) / (self.high_value - self.low_value)
        indicator_height = int(value_percent * thermometer_height)

        # Display the temperature indicator
        self.canvas.create_rectangle(thermometer_x, thermometer_y + thermometer_height - indicator_height,
                                     thermometer_x + thermometer_width, thermometer_y + thermometer_height,
                                     fill="blue", outline="black")

        # Display the temperature value
        self.canvas.create_text(thermometer_x + thermometer_width // 2, thermometer_y + thermometer_height + 10,
                                text=f"{self.temperature}{self.units}",
                                font=("Helvetica", 12, "bold"))

    def update_temperature(self):
        try:
            # Get the new temperature value from the entry
            new_temperature = float(self.entry.get())

            # Check if the new value is within the valid range
            if self.low_value <= new_temperature <= self.high_value:
                self.temperature = new_temperature
                self.update_thermometer()
            else:
                print("Temperature value out of range.")
        except ValueError:
            print("Invalid temperature value.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureDisplayApp(root)
    root.mainloop()
