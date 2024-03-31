import tkinter as tk
from tkinter import ttk
import random

class TemperatureDisplayApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Temperature Display")
        self.geometry("600x400")
        
        # Generate 20 random temperature values
        self.temperature_values = [random.randint(0, 100) for _ in range(20)]
        
        self.init_ui()

    def init_ui(self):
        # Label
        label = ttk.Label(self, text="Enter Range (0-20):")
        label.grid(column=0, row=0, padx=10, pady=10)

        # Entry (Textbox)
        self.entry = ttk.Entry(self)
        self.entry.grid(column=1, row=0, padx=10, pady=10)

        # Button
        button = ttk.Button(self, text="Show", command=self.show_range)
        button.grid(column=2, row=0, padx=10, pady=10)

        # Canvas
        self.canvas = tk.Canvas(self, width=500, height=300)
        self.canvas.grid(column=0, row=1, columnspan=3, padx=10, pady=10)
        
        # Draw initial rectangles and lines
        self.show_range()

    def show_range(self):
        self.canvas.delete("all")
        
        # Get range
        try:
            range_val = int(self.entry.get())
            if range_val < 0 or range_val >= 21:
                raise ValueError
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Invalid range")
            return
        
        # Adjust range to ensure display of last 6 values if entered range is 14-20
        if range_val >= 14:
            range_val = 14

        # Display only 6 values at a time based on the range entered
        temperature_range = self.temperature_values[range_val:range_val+6]

        # Draw rectangles
        bar_width = 30
        bar_spacing = 40
        x_offset = 50
        y_offset = 250
        for i, temp in enumerate(temperature_range):
            x0 = x_offset + (i * (bar_width + bar_spacing))
            y0 = y_offset
            x1 = x0 + bar_width
            y1 = y_offset - temp * 2
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
            self.canvas.create_text(x0 + bar_width//2, y0 + 10, text=str(temp)) # Add temperature labels
        
        # Draw lines
        line_color = "red"
        line_width = 2
        for i in range(len(temperature_range) - 1):
            x0 = x_offset + (i * (bar_width + bar_spacing)) + (bar_width // 2)
            y0 = y_offset - temperature_range[i] * 2
            x1 = x_offset + ((i + 1) * (bar_width + bar_spacing)) + (bar_width // 2)
            y1 = y_offset - temperature_range[i + 1] * 2
            self.canvas.create_line(x0, y0, x1, y1, fill=line_color, width=line_width)
        
        # Draw y-axis
        self.canvas.create_line(x_offset, y_offset, x_offset, 50, arrow=tk.LAST)
        self.canvas.create_text(x_offset - 10, 50, text="Temperature", anchor=tk.E, angle=90)

        # Draw x-axis
        x_axis_offset = 25
        x_axis_y = y_offset + 20
        self.canvas.create_line(x_offset - x_axis_offset, x_axis_y, x_offset + (6 * (bar_width + bar_spacing)) + x_axis_offset, x_axis_y, arrow=tk.LAST)
        self.canvas.create_text(x_offset + (6 * (bar_width + bar_spacing)) + x_axis_offset + 10, x_axis_y, text="Time")

if __name__ == "__main__":
    app = TemperatureDisplayApp()
    app.mainloop()
