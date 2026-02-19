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

window.mainloop()