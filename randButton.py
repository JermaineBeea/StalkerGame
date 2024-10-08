import tkinter
import time
from Template.Button import positionRoot 

def buttonFunc (event = None):
  global count
  count += 1
  button.config(bg = 'red')
  if count == 3: button.config(bg = 'green')


tk_instance = tkinter.Tk()
tk_instance.title('Main Root')
tk_instance.config(bg='black')

x_ratio = 1 / 2
y_ratio = 1 / 2

positionRoot(tk_instance, width_ratio=x_ratio, height_ratio=y_ratio)

# Button initial relative positions to center of widget, and size parameters
x_0 = 0.5
y_0 = 0.5
button_width = 1
button_height = 1

button = tkinter.Button(tk_instance, command = buttonFunc , bg = 'white', width = button_width, height = button_height, 
borderwidth = 2, highlightthickness = 0, activebackground= 'grey', relief = 'raised')
# relif can also equal: flat, sunken, groove, ridge
button.place(relx = x_0, rely = y_0, anchor = 'center')
    

end_time = time.perf_counter()

print(end_time)

tk_instance.mainloop()




