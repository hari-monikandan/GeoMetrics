from tkinter import *
from tkinter import ttk

class Sketchpad(Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.bind("<Button-1>", self.save_posn)
        self.bind("<B1-Motion>", self.add_line)
        self.bind("<Configure>", self.draw_axes)

        self.origin_x = 40
        self.origin_y = 40
        self.tick_spacing = 50
        self.tick_size = 5

    def draw_axes(self, event=None):
        self.delete("axis")
        w = self.winfo_width()
        h = self.winfo_height()

        # X axis (horizontal)
        self.create_line(self.origin_x, h - self.origin_y, w - 10, h - self.origin_y,
                         fill="black", width=2, tags="axis")
        # X axis arrow
        self.create_line(w - 10, h - self.origin_y, w - 18, h - self.origin_y - 5,
                         fill="black", width=2, tags="axis")
        self.create_line(w - 10, h - self.origin_y, w - 18, h - self.origin_y + 5,
                         fill="black", width=2, tags="axis")

        # Y axis (vertical)
        self.create_line(self.origin_x, h - self.origin_y, self.origin_x, 10,
                         fill="black", width=2, tags="axis")
        # Y axis arrow
        self.create_line(self.origin_x, 10, self.origin_x - 5, 18,
                         fill="black", width=2, tags="axis")
        self.create_line(self.origin_x, 10, self.origin_x + 5, 18,
                         fill="black", width=2, tags="axis")

        # X axis ticks and labels
        x = self.origin_x + self.tick_spacing
        count = 1
        while x < w - 10:
            self.create_line(x, h - self.origin_y - self.tick_size,
                             x, h - self.origin_y + self.tick_size,
                             fill="black", tags="axis")
            self.create_text(x, h - self.origin_y + 15, text=str(count * self.tick_spacing),
                             tags="axis")
            x += self.tick_spacing
            count += 1

        # Y axis ticks and labels
        y = h - self.origin_y - self.tick_spacing
        count = 1
        while y > 10:
            self.create_line(self.origin_x - self.tick_size, y,
                             self.origin_x + self.tick_size, y,
                             fill="black", tags="axis")
            self.create_text(self.origin_x - 20, y, text=str(count * self.tick_spacing),
                             tags="axis")
            y -= self.tick_spacing
            count += 1

    def clamp_posn(self, x, y):
        h = self.winfo_height()
        x = max(x, self.origin_x)
        y = min(y, h - self.origin_y)
        return x, y

    def save_posn(self, event):
        self.lastx, self.lasty = self.clamp_posn(event.x, event.y)

    def add_line(self, event):
        x, y = self.clamp_posn(event.x, event.y)
        self.create_line(self.lastx, self.lasty, x, y)
        self.lastx, self.lasty = x, y

root = Tk()
root.title("GeoMetric Calculator")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

sketch = Sketchpad(root)
sketch.grid(column=0, row=0, sticky=(N, W, E, S))

root.mainloop()