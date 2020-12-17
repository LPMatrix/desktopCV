import tkinter
import tkinter.ttk as ttk
import cv2 as cv
import numpy as np
import PIL
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
from datetime import date
from datetime import datetime

window = tkinter.Tk()
window.title("OpenCV Project")
window.geometry("1100x500")
window.config(bg="white")
container=tkinter.Frame(window)
container.config(bg="white")
frame_1 = tkinter.Frame(container) #namelabel
frame_2 = tkinter.Frame(container) #slt_btn for select photo
frame_3 = tkinter.Frame(container) #options menu
frame_4 = tkinter.Frame(container) #mnp btn for image manipulation
frame_6 = tkinter.Frame(window)#image contianer
frame_5a = tkinter.Frame(frame_6) #actual image
frame_5b = tkinter.Frame(frame_6) #altered image
now = datetime.now()

def packs():
    '''
    THIS function packs all the tkinter windows to enable a display
    '''
    container.pack(side="left", padx=40, pady=20)
    frame_1.pack(padx=0, pady=30) #header text
    frame_2.pack(padx=0, pady=10) #select photo
    frame_3.pack(padx=0, pady=10) #drop down menu
    frame_4.pack(padx=0, pady=60) #manipulate button
    frame_6.pack(side="right", padx=10, pady=10, expand = "yes")
    frame_5a.pack(side="left", expand="yes")
    frame_5b.pack(side="right", expand="yes")

welcome = tkinter.Label(master=window,text = F"Welcome Dear! Today is {str(date.today())} and the time is {now.strftime('%H:%M:%S')}",fg="purple", bg="white", width=70)
welcome.config(font=("courier", 13))
welcome.pack()
namelabel = tkinter.Label(master=frame_1, text="Manipulate Image Here", bg="white", fg="purple")
namelabel.config(font=("courier", 17))
namelabel.pack()

def get_img():
    '''
    THIS function:
    -opens images in PIL format
    -displays them on a tkinter window
    -converts the image to cv2 format
    -function is assigned to the Select_Photo buttion
    '''
    global cv_img
    global image_lbl
    global photo
    filename = filedialog.askopenfilename(initialdir="Desktop", title="Select A File", filetype=(("png files","*.png"),("all files","*.*")))
    photo = tkinter.PhotoImage(file=f"{filename}")
    image_lbl = tkinter.Label(frame_5a,image=photo)
    frame_5a.image=photo
    image_lbl.pack(fill="both", expand="yes")
    #conversion
    pil_img=Image.open(f"{filename}")
    numpy_image=np.array(pil_img)
    cv_img = cv.imread(filename)
slt_btn = tkinter.Button(master=frame_2, text = "Select Photo", bg = "white", fg="black", width=20, height=2,command=get_img)
slt_btn.pack()

def del_img():
    '''
    THIS function is for deleting a selected image from tkinter window
    '''
    image_lbl.config(image="")
    image_lbl.image=" "
del_btn = tkinter.Button(master=frame_5a, text = "Remove Photo", bg = "purple", fg="white", width=18, height=2,command=del_img)
del_btn.pack(side = "bottom")

img_opt = ["Sketch", "Blur", "Grayscale", "Rotate", "Erode", "Select Technique"]
techniq = ttk.Combobox(frame_3, values=img_opt)
techniq.config(width=25, height=6)
techniq.current(5)
techniq.pack()

def manip():
    '''
    THIS Function:
    -This function applies various effect to a selected image
    -converts the image to PIL format from cv2 format to enable display in tkinter window
    '''
    global alt_Img_lbl
    global alt_img
    if techniq.get() == "Select Technique":
        messagebox.showinfo("Technique Error", "Please select one of the techniques to manipulate e.g Grayscale.")
    elif techniq.get() == "Rotate":
        alt_img = cv.rotate(cv_img, cv.ROTATE_90_CLOCKWISE)
    elif techniq.get() == "Grayscale":
        alt_img = cv.cvtColor(cv_img, cv.COLOR_BGR2GRAY)
    elif techniq.get() == "Erode":
        kernel = np.ones((6, 6), np.uint8)
        alt_img = cv.erode(cv_img, kernel, cv.BORDER_REFLECT) 
    elif techniq.get() == "Blur":
        alt_img = cv.blur(cv_img, (10, 10))
    elif techniq.get() == "Sketch":
        alt_img = cv.Canny(cv_img,50,100)
    else:
        messagebox.showinfo("Technique Error", "Sorry, the technique you clicked is not yet activated")
    alt_img = cv.cvtColor(alt_img, cv.COLOR_BGR2RGB)
    tk_img = Image.fromarray(alt_img)
    tk_img = ImageTk.PhotoImage(tk_img)
    alt_Img_lbl = tkinter.Label(frame_5b,image=tk_img)
    frame_5b.image=tk_img
    alt_Img_lbl.pack()

mnp_btn = tkinter.Button(master=frame_4, text = "Manipulate", bg = "purple", fg="white", width=16, height=2, command=manip)
mnp_btn.pack()

def clear_eff():
    '''
    This function clears the altared image
    '''
    alt_Img_lbl.config(image="")
    alt_Img_lbl.image=" "
clr_btn = tkinter.Button(master=frame_5b, text = "Clear Effect", bg = "purple", fg="white", width=18, height=2,command=clear_eff)
clr_btn.pack(side = "bottom")

packs()
window.mainloop()