import tkinter
from Template.Button import positionRoot  # Assuming you have the positionRoot function in Button.py

tk_instance = tkinter.Tk()
tk_instance.title('Main Root')
tk_instance.config(bg='white')
x_ratio = 1 / 2
y_ratio = 1 / 2
positionRoot(tk_instance, width_ratio=x_ratio, height_ratio=y_ratio)


