import tkinter
from Template.Button import positionRoot  # Assuming you have the positionRoot function in Button.py

tk_instance = tkinter.Tk()
tk_instance.title('Main Root')
tk_instance.config(bg='white')
x_ratio = 1 / 2
y_ratio = 1 / 2
positionRoot(tk_instance, width_ratio=x_ratio, height_ratio=y_ratio)

canvas = tkinter.Canvas(tk_instance, bg='black')
canvas.pack(fill='both', expand=True, padx=20, pady=20)

# Icon dimensions
icon_dimension = 10

def center_icon():
    # Get the width and height of the canvas after rendering
    x_0 = (canvas.winfo_width() - icon_dimension) // 2
    y_0 = (canvas.winfo_height() - icon_dimension) // 2
    
    # Create the icon at the center
    canvas.create_oval(x_0, y_0, x_0 + icon_dimension, y_0 + icon_dimension, fill='red', outline='white')

# Call center_icon after a delay to ensure the window is rendered
tk_instance.after(100, center_icon)

tk_instance.mainloop()
