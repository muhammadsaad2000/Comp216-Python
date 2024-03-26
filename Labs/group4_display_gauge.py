import tkinter as tk
from tkinter import ttk
import math
import random

class SensorDisplayGUI(tk.Tk):
    def __init__(self, sensor_name, units, low_value, normal_range, high_value):
        super().__init__()
        self.title(f"{sensor_name} Display")
        self.geometry("600x400")

        self.sensor_name = sensor_name
        self.units = units
        self.low_value = low_value
        self.normal_range = normal_range
        self.high_value = high_value

        self.current_value = tk.DoubleVar()
        self.current_value.set(self.normal_range[0])

        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self)
        frame.pack(fill=tk.BOTH, expand=True)

        # Circular Gauge
        self.gauge_canvas = tk.Canvas(frame, width=200, height=200)
        self.gauge_canvas.pack(pady=20)

        # Label for displaying sensor value
        self.value_label = ttk.Label(frame, textvariable=self.current_value, font=('Helvetica', 24))
        self.value_label.pack()

        # Entry and Button for changing value
        self.value_entry = ttk.Entry(frame, textvariable=self.current_value, font=('Helvetica', 12))
        self.value_entry.pack()
        self.update_button = ttk.Button(frame, text="Update", command=self.update_value)
        self.update_button.pack()

        # Additional information
        info_label = ttk.Label(frame, text=f"Units: {self.units}\nLow: {self.low_value} | Normal Range: {self.normal_range[0]}-{self.normal_range[1]} | High: {self.high_value}")
        info_label.pack()

        # Draw the circular gauge initially
        self.draw_gauge()

    def draw_gauge(self):
        self.gauge_canvas.delete("all")
        gauge_radius = 80
        center_x = 100
        center_y = 100
        value = self.current_value.get()

        start_angle = -135
        extent_angle = 270

        self.gauge_canvas.create_arc(center_x - gauge_radius, center_y - gauge_radius,
                                     center_x + gauge_radius, center_y + gauge_radius,
                                     start=start_angle, extent=extent_angle, outline="#808080", width=8)

        # Calculate the position for the needle based on the current value
        angle = start_angle + (extent_angle * (value - self.low_value) / (self.high_value - self.low_value))
        needle_x = center_x + (gauge_radius - 10) * math.cos(math.radians(angle))
        needle_y = center_y + (gauge_radius - 10) * math.sin(math.radians(angle))

        self.gauge_canvas.create_line(center_x, center_y, needle_x, needle_y, fill="red", width=2)

    def update_value(self):
        # Ensure the entered value is within the valid range
        new_value = self.current_value.get()
        if self.low_value <= new_value <= self.high_value:
            self.draw_gauge()
        else:
            # Reset value to within the valid range
            self.current_value.set(max(self.low_value, min(new_value, self.high_value)))


# Example usage:
if __name__ == "__main__":
    sensor_name = "Temperature"
    units = "°C"
    low_value = 0
    normal_range = (10, 30)
    high_value = 40

    app = SensorDisplayGUI(sensor_name, units, low_value, normal_range, high_value)
    app.mainloop()
