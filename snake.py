import random
import tkinter

ROWS = 25
COLUMNS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * COLUMNS 
WINDOW_HEIGHT = TILE_SIZE * ROWS 

# Game Window

window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False) # FIxed window width and height

# Master is window
canvas = tkinter.Canvas(window, 
                        bg = "black", 
                        width = WINDOW_WIDTH, 
                        height = WINDOW_HEIGHT, 
                        borderwidth = 0,
                        highlightthickness = 0)
canvas.pack()
window.update()

# Centering the Window

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width - window_width) / 2)
window_y = int((screen_height - window_height) / 2)

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()