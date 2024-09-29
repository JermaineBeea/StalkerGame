import tkinter
from Button import positionRoot

tk_instance = tkinter.Tk()
tk_instance.title('Main Root')
tk_instance.config(bg = 'white')
x_ratio = 1/2; y_ratio = 1/2
positionRoot(tk_instance, width_ratio = x_ratio, height_ratio = y_ratio)

canvas = tkinter.Canvas(tk_instance, bg = 'black')
canvas.pack(fill = 'both', expand = True)
canvas.pack(padx = 20, pady = 20)

icon_dimension = 100
# Starting positions
x_0 = canvas.winfo_width()//2
y_0 = canvas.winfo_height()//2
dimension = 10

icon = canvas.create_oval(x_0, y_0, x_0 + dimension, y_0 + dimension, fill = 'red', outline = 'white')

tk_instance.mainloop()