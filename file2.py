
#Using iconphoto()
#This method allows you to use various image formats like .png or .gif:

import tkinter
from tkinter import PhotoImage

# Create the main application window
root = tkinter.Tk()
root.title('My Tkinter App')

# Set the window icon (for .png or .gif)
icon_image = PhotoImage(file='001.jpg')  # Replace with your .png file path
root.iconphoto(True, icon_image)

# Run the application
root.mainloop()
