import tkinter as tk

canvas_width=600
canvas_height=300
canvas_background='white'
start_x=0
start_y=0
rectangle_size=100
rectangle_fill="red"
rectangle_outline="red"

x_direction = 1
y_direction = 1

move = 1 #px
move_every = 3 #millisecond

root = tk.Tk()
canvas = tk.Canvas(root, width = canvas_width, height = canvas_height,bg=canvas_background)
canvas.pack()

rect = canvas.create_rectangle(start_x,start_y,start_x+rectangle_size,start_y+rectangle_size, fill=rectangle_fill,outline=rectangle_outline)

def move_rect():
    global x_direction,y_direction,rectangle_size
    canvas.move(rect, (move * x_direction), (move * y_direction))
    canvas.after(move_every, move_rect)

    coords = canvas.coords(rect)
    x = coords[0]
    y = coords[1]

    if((x+rectangle_size) >= canvas_width):
        x_direction = -1
    if(x <= 0):
        x_direction = 1
    if((y+rectangle_size) >= canvas_height):
        y_direction = -1
    if(y <= 0):
        y_direction = 1
        
move_rect()

root.mainloop()