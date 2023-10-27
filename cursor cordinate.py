import pyautogui
import tkinter as tk

def get_cursor_coordinates(event=None):
    x, y = pyautogui.position()
    coordinates_label.config(text=f"X: {x}, Y: {y}")
    
window = tk.Tk()
window.title("Cursor Coordinates App")

coordinates_label = tk.Label(window, text="")
coordinates_label.pack()

#Get cursor cordinates after pressing Space button
window.bind("<space>", get_cursor_coordinates)

window.mainloop()
