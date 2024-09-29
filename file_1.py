import tkinter

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

# Initialize the main Tkinter window
tk_root = tkinter.Tk()
tk_root.title('Main Root')
width_ratio = 1/2
height_ratio = 1/2
positionRoot(tk_root, width_ratio, height_ratio)

# Initial button position and dimensions
button_dimensions = 1
b_x = 0.5
b_y = 0.5
shift_speed = 0.05

# Create a button
button = tkinter.Button(tk_root, bg='red', width=button_dimensions, height=button_dimensions)
button.place(relx=b_x, rely=b_y, anchor='center')

# Function to move the button based on keypress events
def moveButton(event):
    global b_x, b_y
    if event.keysym in ('Left', 'W'):
        b_x = max(0, b_x - shift_speed)
    if event.keysym in ('Right', 'D'):
        b_x = min(1, b_x + shift_speed)
    if event.keysym == 'Up':
        b_y = max(0, b_y - shift_speed)
    if event.keysym == 'Down':
        b_y = min(1, b_y + shift_speed)

    # Reposition the button using the updated coordinates
    button.place(relx=b_x, rely=b_y, anchor='center')

# Bind arrow keys to move the button
tk_root.bind('<Left>', moveButton)
tk_root.bind('<Right>', moveButton)
tk_root.bind('<Up>', moveButton)
tk_root.bind('<Down>', moveButton)

# Start the Tkinter main event loop
tk_root.mainloop()
