import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root, width = 600, height = 300,bg="white")
canvas.pack()
rect = canvas.create_rectangle(0,0,100,100, fill="red",outline="red")
def move_rect():
    x_direction = 1
    y_direction = 1
    canvas.move(rect,  x_direction, y_direction)
    canvas.after(3, move_rect)
    coords = canvas.coords(rect)
    x = coords[0]
    y = coords[1]
    if((x+100) >= 600):
        x_direction = -1
    if(x <= 0):
        x_direction = 1
    if((y+100) >= 300):
        y_direction = -1
    if(y <= 0):
        y_direction = 1
move_rect()
root.mainloop()