import tkinter as tk

root = tk.Tk()
root.title("Cursor Tracker")
root.geometry("400x300")

label = tk.Label(root, text="Move your cursor around!")
label.pack(pady=50)

def on_mouse_motion(event):
    x, y = event.x, event.y
    label.configure(text=f"Cursor Position: ({x}, {y})")

root.bind('<Motion>', on_mouse_motion)
root.mainloop()