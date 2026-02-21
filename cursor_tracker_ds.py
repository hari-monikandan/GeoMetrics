# # Need to write a code that can track (x,y) coordinates and find circumference in pixels.
# # There should also be an option to set a scale to get answer in physical units
 
# # The package pyautogui seems to be a nice method to retreive mouse positions.
# import pyautogui
# import matplotlib.pyplot as plt
# import numpy as np
# # Package keyboard to recognise a key being pressed on.
# import keyboard
# import time
# from tkinter import *

# print('Press Ctrl-C to quit.')
# list_coordinates = []

# try:
#     while True:
#         x, y = pyautogui.position()
#         # positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         # print(positionStr, end='')
#         # print('\b' * len(positionStr), end='')
#         if keyboard.is_pressed('q'):
#             list_coordinates.append((x, y))

# except KeyboardInterrupt:
#     plt.plot([(x[0]) for x in list_coordinates], [(1079 - y[1]) for y in list_coordinates])
#     plt.show()
#     print('\n')

# def distance_finder(point1, point2):
#     return np.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

# # Currently this model relies on having to draw a shape in one continuos stroke
# # Can take a break by leaving key 'q' but, need to resume 'q' from same place
# # In order to get correct answer and allow flexibility, need to introduce the idea of 'multiple strokes'
# # and only calculate distances within a stroke and sum the strokes later.

# small_dists = [distance_finder(list_coordinates[i], list_coordinates[i+1]) for i in range(0, len(list_coordinates)-1)]

# print(sum(small_dists))

from tkinter import *
from tkinter import ttk

class Sketchpad(Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.margin = 50

        self.bind("<Button-1>", self.save_posn)
        self.bind("<B1-Motion>", self.add_line)
        self.bind("<Configure>", self.draw_axes)

    def draw_axes(self, event=None):
        self.delete("axes")
        w = self.winfo_width()
        h = self.winfo_height()
        m = self.margin

        self.create_line(m, h - m, w - m, h - m, width=2, arrow=LAST, tags="axes")
        self.create_line(m, h - m, m, m, width=2, arrow=LAST, tags="axes")

    def save_posn(self, event):
        self.lastx, self.lasty = event.x, event.y

    def add_line(self, event):
        self.create_line(self.lastx, self.lasty, event.x, event.y)
        self.save_posn(event)

root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

sketch = Sketchpad(root)
sketch.grid(column=0, row=0, sticky=(N, W, E, S))

root.mainloop()