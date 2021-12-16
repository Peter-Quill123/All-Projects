from PIL import Image, ImageDraw
from tkinter import mainloop, Tk, Canvas, PhotoImage, NW
import os 
 
img = Image.new('RGB', (250, 80), color = (73, 109, 137))
 
d = ImageDraw.Draw(img)
d.text((30,30), "Hello World", fill=(255,255,0))
 
img.save("1.png")

root = Tk()      

canvas = Canvas(root, width = 300, height = 100)      
canvas.pack()      
img = PhotoImage(file="1.png")      
canvas.create_image(20,20, anchor=NW, image=img)      
root.title = "CaptCha"
mainloop() 

os.system('del 1.png')