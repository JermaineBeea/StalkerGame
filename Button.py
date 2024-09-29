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

if __name__ == '__main__':

  tk_root = tkinter.Tk()
  tk_root.title('Main Root')
  width_ratio = 1/2
  height_ratio = 1/2
  positionRoot(tk_root, width_ratio, height_ratio)

  button_dimensions = 1
  b_x = 0.5
  b_y = 0.5
  shift_speed = 0.05

  button = tkinter.Button(tk_root, bg='red', width=button_dimensions, height=button_dimensions)
  button.place(relx=b_x, rely=b_y, anchor='center')

  # Button co-ordinates
  b_posX = button.winfo_width()
  b_posY = button.winfo_height()

  def moveButton(event):
      global b_x, b_y
      if event.keysym in ('Left', 'a'):
          b_x = max(0, b_x - shift_speed)
      if event.keysym in ('Right', 'd'):
          b_x = min(1, b_x + shift_speed)
      if event.keysym in ('Up', 'w'):
          b_y = max(0, b_y - shift_speed)
      if event.keysym in ('Down', 's'):
          b_y = min(1, b_y + shift_speed)

      # Reposition the button using the updated coordinates
      button.place(relx=b_x, rely=b_y, anchor='center')

  tk_root.bind('<Left>', moveButton)
  tk_root.bind('<Right>', moveButton)
  tk_root.bind('<Up>', moveButton)
  tk_root.bind('<Down>', moveButton)
  tk_root.bind('<a>', moveButton)
  tk_root.bind('<d>', moveButton)
  tk_root.bind('<w>', moveButton)
  tk_root.bind('<s>', moveButton)

  tk_root.mainloop()
