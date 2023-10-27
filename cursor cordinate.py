import pyautogui
import tkinter as tk

def get_cursor_coordinates(event=None):
    x, y = pyautogui.position()
    coordinates_label.config(text=f"X: {x}, Y: {y}")

# Create a tkinter window
window = tk.Tk()
window.title("Cursor Coordinates App")

# Create a label to display coordinates
coordinates_label = tk.Label(window, text="")
coordinates_label.pack()

# Bind the "Space" key press to get_cursor_coordinates function
window.bind("<space>", get_cursor_coordinates)

# Start the tkinter main loop
window.mainloop()