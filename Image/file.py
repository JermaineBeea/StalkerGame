#Using iconbitmap()
#This method allows you to set an icon from a .ico file:

import tkinter

# Create the main application window
root = tkinter.Tk()
root.title('My Tkinter App')

# Set the window icon
root.iconbitmap('001.ico')  # Replace with your .ico file path

# Run the application
root.mainloop()
