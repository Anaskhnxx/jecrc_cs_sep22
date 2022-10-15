import pandas as pd
import tkinter as ttk
import seaborn as sns
from tkinter import*
from PIL import Image,ImageTk

win = ttk.Tk()
win.geometry('750x250')
win.title('Canvas')

# create a canvas
canvas = ttk.Canvas(win, width = 600 , height = 400 )
canvas.pack()

# Load an image in the script

img = ttk.ImageTk.PhotoImage(Image.open('mygraph.png'))


# add image to the canvas items 
canvas.create_image(10,10,anchor=NW ,image=img)



win.mainloop()

