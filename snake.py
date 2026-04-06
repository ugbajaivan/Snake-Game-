import random
import tkinter

ROWS = 25
COLUMNS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * COLUMNS 
WINDOW_HEIGHT = TILE_SIZE * ROWS 

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y


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

# Format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Initialize Game
snake = Tile(5*TILE_SIZE,5*TILE_SIZE) # Single tile for snake's head
food = Tile(10*TILE_SIZE,10*TILE_SIZE)

# Variables for Key listener
velocity_x=0
velocity_y=0


def change_direction(e): # e is event
    #print(e)
    #print(e.keysym)
    global velocity_x, velocity_y
    
    if e.keysym == "Up" and velocity_y != 1:
        velocity_x = 0
        velocity_y = -1
    if e.keysym == "Down" and velocity_y != -1:
        velocity_x = 0
        velocity_y = 1
    if e.keysym == "Left" and velocity_x != 1:
        velocity_x = -1
        velocity_y = 0
    if e.keysym == "Right" and velocity_x != -1:
        velocity_x = 1
        velocity_y = 0


def move():
    global snake
    
    snake.x += velocity_x*TILE_SIZE
    snake.y += velocity_y*TILE_SIZE


def draw():
    global snake # Referencing external snake variable and not a local one in function
    move()
    
    canvas.delete("all")
    
    # Draw Snake
    canvas.create_rectangle(snake.x, snake.y, (snake.x + TILE_SIZE), (snake.y + TILE_SIZE), fill= "lime green")
    
    # Draw Food
    canvas.create_rectangle(food.x, food.y, (food.x + TILE_SIZE), (food.y + TILE_SIZE), fill= "red")
    
    window.after(100, draw) # Every 100ms, snake will be drawn. AKA Running at 10 fps
    
draw()
window.bind("<KeyRelease>", change_direction)
window.mainloop()