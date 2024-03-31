import tkinter as tk
from tkinter import ttk, Canvas, Label
import random
import threading
import time

class WeatherDisplayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic Weather Display App")

        # List of 20 random values
        self.values = [random.randint(0, 100) for _ in range(20)]

        # Box for drawing the chart
        self.chart_canvas = Canvas(self.root, width=600, height=300, bg="white", highlightbackground="black", highlightthickness=1)
        self.chart_canvas.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Initialize UI and start the update thread
        self.init_ui()

    def init_ui(self):
        # Removing the Entry widget as it is not used in this application

        # Initialize the update thread for dynamic chart updates
        update_thread = threading.Thread(target=self.update_values_loop, daemon=True)
        update_thread.start()

    def update_values_loop(self):
        """Update values in a loop and redraw the chart."""
        while True:
            # Update dataset
            self.values.pop(0)
            self.values.append(random.randint(0, 100))

            # Redraw the chart on the canvas
            self.draw_chart(self.values)

            # Wait for 0.5 second before the next update
            time.sleep(0.5)

    def draw_chart(self, values):
        """Draw a line chart based on the values."""
        # Clear the canvas
        self.chart_canvas.delete("all")

        # Calculate coordinates for drawing lines
        max_value = max(values) if values else 100  # Prevent division by zero
        min_value = min(values) if values else 0
        canvas_width = int(self.chart_canvas.cget("width"))
        canvas_height = int(self.chart_canvas.cget("height"))
        x_spacing = canvas_width / (len(values) - 1 or 1)
        y_scaling = (canvas_height - 20) / (max_value - min_value or 1)

        # Draw lines
        for i in range(len(values) - 1):
            x1 = i * x_spacing
            y1 = canvas_height - ((values[i] - min_value) * y_scaling)
            x2 = (i + 1) * x_spacing
            y2 = canvas_height - ((values[i + 1] - min_value) * y_scaling)
            self.chart_canvas.create_line(x1, y1, x2, y2, fill="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherDisplayApp(root)
    root.mainloop()
