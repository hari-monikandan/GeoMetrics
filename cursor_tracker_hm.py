# Hari's work
# Creating a Tkinter GUI to track cursor movement and find distance traveled by cursor
import tkinter as tk
import pyautogui as pag
import random

def mover(root):
    screen_width, screen_height = pag.size()
    x = random.randint(100, screen_width-100)
    y = random.randint(100, screen_height-100)

    pag.moveTo(x, y, duration=0.5)

    root.after(5000, lambda: mover(root))

root = tk.Tk()
root.title("Cursor Tracker")
root.geometry("300x200")

label = tk.Label(root, text="Tracking cursor movement...")
label.pack(pady=20)

mover(root)

root.mainloop()