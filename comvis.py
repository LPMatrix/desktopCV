import os, sys
import tkinter
import tkinter.ttk
import cv2 as cv
from tkinter import filedialog
from PIL import Image
from datetime import date
from datetime import datetime

window = tkinter.Tk()
window.title("OpenCV Project")
window.geometry("1000x500")
window.config(bg="white")
container=tkinter.Frame(window, width=2200, height=500)
container.config(bg="white")
frame_1 = tkinter.Frame(container) #namelabel
frame_2 = tkinter.Frame(container) #slt_btn for select photo
frame_3 = tkinter.Frame(container) #options menu
frame_4 = tkinter.Frame(container) #mnp btn for image manipulation
frame_6 = tkinter.Frame(window)#image frame
now = datetime.now()

def packs():
    container.pack(side="left", padx=40, pady=20)
    frame_1.pack(padx=0, pady=30) #header text
    frame_2.pack(padx=0, pady=10) #select photo
    frame_3.pack(padx=0, pady=10) #drop down menu
    frame_4.pack(padx=0, pady=60) #manipulate button
    frame_6.pack(side="right", padx=20, pady=20, expand = "yes")

welcome = tkinter.Label(master=window,text = F"Welcome Dear! Today is {str(date.today())} and the time is {now.strftime('%H:%M:%S')}",fg="purple", bg="white", width=70)
welcome.config(font=("courier", 13))
welcome.pack()
namelabel = tkinter.Label(master=frame_1, text="Manipulate Image Here", bg="white", fg="purple")
namelabel.config(font=("courier", 17))
namelabel.pack()

imgopt = ["Sketch", "Sharpen", "Blur", "Rotate", "Grayscale", "Select Technique"]
var = tkinter.StringVar()
var.set("Select Technique")
slteff = tkinter.OptionMenu(frame_3, var, *imgopt)
slteff.config(width=20, height=2, fg="black", bg="white")
slteff.pack()
mnp_btn = tkinter.Button(master=frame_4, text = "Manipulate", bg = "purple", fg="white", width=16, height=2)
mnp_btn.pack()

#event functions (handlers)
def get_img():
    filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =(("jpeg files","*.png"),("all files","*.*")))
    photo = tkinter.PhotoImage(file=f"{filename}")
    #photo=photo.resize(290, 263)
    global image_lbl
    image_lbl = tkinter.Label(frame_6,image=photo)
    frame_6.image=photo
    image_lbl.pack(fill="both", expand="yes")
slt_btn = tkinter.Button(master=frame_2, text = "Select Photo", bg = "white", fg="black", width=20, height=2,command=get_img)
slt_btn.pack()

def del_img():
    image_lbl.config(image="")
    image_lbl.image=" "

del_btn = tkinter.Button(master=frame_6, text = "Remove Photo", bg = "purple", fg="white", width=18, height=2,command=del_img)
del_btn.pack(side = "bottom")

packs()
window.mainloop()