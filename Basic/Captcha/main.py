from PIL import Image, ImageDraw
from tkinter import mainloop, Tk, Canvas, PhotoImage, NW
import os 
import random

def captcha():
    character = ['1', '2', '3', '4', '5', '6',
                 '7', '8', '9', '0', 'a', 'b',
                 'c', 'd', 'e', 'f', 'g', 'h',
                 'i', 'j', 'k', 'l', 'm', 'n',
                 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x','y', 'z'] 
    rn1 = random.randint(0,35) 
    rn2 = random.randint(0,35) 
    rn3 = random.randint(0,35) 
    rn4 = random.randint(0,35) 
    rn5 = random.randint(0,35) 
    rn6 = random.randint(0,35) 
    rn7 = random.randint(0,35) 
    ch1 = character[rn1]
    ch2 = character[rn2]
    ch3 = character[rn3]
    ch4 = character[rn4]
    ch5 = character[rn5]
    ch6 = character[rn6]
    ch7 = character[rn7]
    captchacode = ch1+ch2+ch3+ch4+ch5+ch6+ch7
    return captchacode
 
img = Image.new('RGB', (250, 80), color = (73, 109, 137))

d = ImageDraw.Draw(img)
d.text((30,30), text = captcha(), fill=(255,255,0))
 
img.save("1.png")

root = Tk()      

canvas = Canvas(root, width = 300, height = 100)      
canvas.pack()      
img = PhotoImage(file="1.png")      
canvas.create_image(20,20, anchor=NW, image=img)      
root.title("CaptCha")
root.resizable(False,False)
mainloop() 

os.system('del 1.png')