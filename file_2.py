import tkinter

def positionRoot(root, width_ratio=1/2, height_ratio=1/2, x_driftRatio=0, y_driftRatio=0):
    """ 
    This function modifies the widget width and length relative to screen width and height.
    And modifies the position on screen relative to the center of the screen.
    
    Args: 
        width_ratio (float: default 1/2): The width (x-axis) of the root widget as a fraction of the screen width.
        height_ratio (float: default 1/2): The height (y-axis) of the root widget as a fraction of the screen height.
        x_driftRatio (float: default 0): The x-axis deviation (+ for 'right', - for 'left') from center, 
                                         represented as a fraction of the maximum x-axis deviation (screen width//2).
        y_driftRatio (float: default 0): The y-axis deviation (+ for 'down', - for 'up') from center, 
                                         represented as a fraction of the maximum y-axis absolute deviation (screen height//2).
    
    Returns:
        Function has no return, as it modifies root in place.
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


# Initialize the Tkinter root window
tk_root = tkinter.Tk()
tk_root.title('Main Root')
positionRoot(tk_root, 1/2, 1/2)

# Button dimensions and initial placement
button_dimensions = 1
button = tkinter.Button(tk_root, bg='red', width=button_dimensions, height=button_dimensions)
button.pack(padx=0, pady=0)
button.place(relx=0.5, rely=0.5, anchor='center')

# Movement parameters
button_speed = 0.05  # Change this value for faster or slower movement
current_x = 0.5  # Initial horizontal position (50% of the window)
current_y = 0.5  # Initial vertical position (50% of the window)

# Function to move the button
def moveButton(event):
    global current_x, current_y

    if event.keysym == 'Left':
        current_x = max(current_x - button_speed, 0)  # Prevent moving out of bounds
    elif event.keysym == 'Right':
        current_x = min(current_x + button_speed, 1)  # Prevent moving out of bounds
    elif event.keysym == 'Up':
        current_y = max(current_y - button_speed, 0)  # Prevent moving out of bounds
    elif event.keysym == 'Down':
        current_y = min(current_y + button_speed, 1)  # Prevent moving out of bounds

    button.place(relx=current_x, rely=current_y, anchor='center')

# Binding the arrow keys to move the button
tk_root.bind('<Left>', moveButton)
tk_root.bind('<Right>', moveButton)
tk_root.bind('<Up>', moveButton)
tk_root.bind('<Down>', moveButton)

tk_root.mainloop()
