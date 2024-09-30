import tkinter
import time
from Template.Button import positionRoot 
tk_instance = tkinter.Tk()
tk_instance.title('Main Root')
tk_instance.config(bg='grey')

def buttonFunc (event = None):
  button.config(bg = 'red')

def timeEvent ():
  start_time = time.perf_counter()
  
x_ratio = 1 / 2
y_ratio = 1 / 2

positionRoot(tk_instance, width_ratio=x_ratio, height_ratio=y_ratio)

# Button initial relative positions to center of widget, and size parameters
x_0 = 0.5
y_0 = 0.5
button_width = 1
button_height = 1

button = tkinter.Button(tk_instance, command = buttonFunc , bg = 'white', width = button_width, height = button_height, 
borderwidth = 2, highlightthickness = 0, activebackground= 'blue', relief = 'raised')
# relif can also equal: flat, sunken, groove, ridge
button.place(relx = x_0, rely = y_0, anchor = 'center')
    
tk_instance.bind('<Button-3>', buttonFunc)

tk_instance.mainloop()




