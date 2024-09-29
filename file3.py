#2. Adding an Icon to Buttons or Other Widgets
#If you want to add an icon to a button, you can use the PhotoImage class in the same way:

#python
#Copy code
import tkinter
from tkinter import PhotoImage

# Create the main application window
root = tkinter.Tk()
root.title('My Tkinter App')

# Load the button icon
button_icon = PhotoImage(file='path_to_button_icon.png')  # Replace with your .png file path

# Create a button with an icon
button = tkinter.Button(root, image=button_icon, command=lambda: print("Button Clicked"))
button.pack(pady=20)

# Run the application
root.mainloop()