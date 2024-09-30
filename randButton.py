import tkinter
from Template.Button import positionRoot  # Assuming you have the positionRoot function in Button.py

tk_instance = tkinter.Tk()
tk_instance.title('Main Root')
tk_instance.config(bg='grey')

x_ratio = 1 / 2
y_ratio = 1 / 2

positionRoot(tk_instance, width_ratio=x_ratio, height_ratio=y_ratio)

# Button initial relative positions to center of widget, and size parameters
x_0 = 0.5
y_0 = 0.5
button_width = 1
button_height = 1

def buttonFunc (event = None):
  global bg_colour
  bg_colour = 'red'
  buttonCharacteristics()

def buttonCharacteristics():
  bg_colour = 'white'
  button = tkinter.Button(tk_instance, command = buttonFunc , bg = bg_colour, width = button_width, height = button_height, 
  borderwidth = 2, highlightthickness = 0, activebackground= 'blue', relief = 'raised')
# relif can also equal: flat, sunken, groove, ridge
  button.place(relx = x_0, rely = y_0, anchor = 'center')
  
buttonCharacteristics()
  
tk_instance.bind('<Button-3>', buttonFunc)

tk_instance.mainloop()




