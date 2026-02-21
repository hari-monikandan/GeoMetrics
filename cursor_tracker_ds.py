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

import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import mouse

root = tk.Tk()
root.title("Cursor Tracker")
root.geometry("400x300")

label = tk.Label(root, text="Move your cursor around!")
label.pack(pady=50)

list_coordinates = []

def mouse_click(event):
    height = root.winfo_height()
    x, y = event.x, height - event.y
    list_coordinates.append((x, y))

def on_mouse_motion(event):
    height = root.winfo_height()
    x, y = event.x, height - event.y
    label.configure(text=f"Cursor Position: ({x}, {y})")
    
    # 0x0100 = left mouse button held
    if event.state & 0x0100:
        list_coordinates.append((x, y))

#root.bind("<Button-1>", mouse_click)
#root.bind("<B1-Motion>", mouse_click) 

root.bind('<Motion>', on_mouse_motion)
root.mainloop()

def distance_finder(point1, point2):
     return np.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

small_dists = [distance_finder(list_coordinates[i], list_coordinates[i+1]) for i in range(0, len(list_coordinates)-1)]

print(sum(small_dists))