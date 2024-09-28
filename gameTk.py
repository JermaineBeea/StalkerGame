import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Move Icon with Arrow Keys")

# Set up the canvas
canvas_width, canvas_height = 800, 600
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Define the icon (a square)
icon_size = 50
icon_x, icon_y = canvas_width // 2, canvas_height // 2
icon = canvas.create_rectangle(icon_x, icon_y, icon_x + icon_size, icon_y + icon_size, fill="blue")

# Define the speed
icon_speed = 15

# Function to handle key presses
def move_icon(event):
    x, y = 0, 0
    
    # Move the icon based on the arrow keys pressed
    if event.keysym == 'Left':
        x = -icon_speed
    elif event.keysym == 'Right':
        x = icon_speed
    elif event.keysym == 'Up':
        y = -icon_speed
    elif event.keysym == 'Down':
        y = icon_speed

    # Get current position of the icon
    current_position = canvas.coords(icon)
    
    # Calculate new position
    new_x1 = max(0, min(current_position[0] + x, canvas_width - icon_size))
    new_y1 = max(0, min(current_position[1] + y, canvas_height - icon_size))
    new_x2 = new_x1 + icon_size
    new_y2 = new_y1 + icon_size

    # Move the icon to the new position
    canvas.coords(icon, new_x1, new_y1, new_x2, new_y2)

# Bind arrow keys to the move_icon function
root.bind('<Left>', move_icon)
root.bind('<Right>', move_icon)
root.bind('<Up>', move_icon)
root.bind('<Down>', move_icon)

# Start the Tkinter event loop
root.mainloop()
