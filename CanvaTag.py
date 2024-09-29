import tkinter
from tkinter import PhotoImage

def positionRoot(root, width_ratio=1/2, height_ratio=1/2, x_driftRatio=0, y_driftRatio=0):
    """ 
    This function modifies the widget width and height relative to screen size
    and positions it on screen relative to the center.
    """
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    screen_centerX = screen_width // 2
    screen_centerY = screen_height // 2

    root_width = int(screen_width * width_ratio)
    root_height = int(screen_height * height_ratio)

    root_centerX = root_width // 2
    root_centerY = root_height // 2

    screen_centerX = int(screen_centerX * (1 + x_driftRatio))
    screen_centerY = int(screen_centerY * (1 + y_driftRatio))

    root_x_change = screen_centerX - root_centerX
    root_y_change = screen_centerY - root_centerY

    root.geometry(f'{root_width}x{root_height}+{root_x_change}+{root_y_change}')

tk_root = tkinter.Tk()
tk_root.title('Main Root')
width_ratio = 1/2
height_ratio = 1/2
positionRoot(tk_root, width_ratio, height_ratio)

canvas = tkinter.Canvas(tk_root, bg = 'grey')
canvas.pack(fill = 'both', expand = True)

icon_dimensions = 1
n_x = 0
n_y = 0
shift_speed = 0.05

icon = canvas.create_oval(10, 10, 30, 30, fill='red')

def on_click(event):
    print("Circular button clicked!")

# canvas.tag_bind(icon, "<Button-1>", on_click)

def moveButton(event):
    icon_posX = canvas.coords(icon)
    
    if event.keysym == 'Left':
        canvas.move(icon, -10, 0)
    elif event.keysym == 'Right':
        canvas.move(icon, 10, 0)
    elif event.keysym == 'Up':
        canvas.move(icon, 0, -10)
    elif event.keysym == 'Down':
        canvas.move(icon, 0, 10)

tk_root.bind('<Left>', moveButton)
tk_root.bind('<Right>', moveButton)
tk_root.bind('<Up>', moveButton)
tk_root.bind('<Down>', moveButton)
tk_root.bind('<a>', moveButton)
tk_root.bind('<d>', moveButton)
tk_root.bind('<w>', moveButton)
tk_root.bind('<s>', moveButton)

# Start the Tkinter main event loop
tk_root.mainloop()
