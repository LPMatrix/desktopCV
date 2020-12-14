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

cv_img = None
def get_img():
    global cv_img
    global image_lbl
    global photo
    filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=(("png files","*.png"),("all files","*.*")))
    photo = tkinter.PhotoImage(file=f"{filename}")
    image_lbl = tkinter.Label(frame_6,image=photo)
    frame_6.image=photo
    image_lbl.pack(fill="both", expand="yes")
    #conversion
    pil_img=Image.open(f"{filename}")
    numpy_image=np.array(pil_img)
    # cv_img = cv.cvtColor(np.float32(numpy_image), cv.COLOR_RGB2BGR)
    # cv_img = np.float32(numpy_image)
    # print(pil_img)
    cv_img = cv.imread(filename)

slt_btn = tkinter.Button(master=frame_2, text = "Select Photo", bg = "white", fg="black", width=20, height=2,command=get_img)
slt_btn.pack()

def del_img():
    image_lbl.config(image="")
    image_lbl.image=" "
del_btn = tkinter.Button(master=frame_6, text = "Remove Photo", bg = "purple", fg="white", width=18, height=2,command=del_img)
del_btn.pack(side = "bottom")

img_opt = ["Sketch", "Sharpen", "Blur", "Grayscale", "Rotate", "Select Technique"]
techniq = ttk.Combobox(frame_3, values=img_opt)
techniq.config(width=25, height=6)
techniq.current(5)
techniq.pack()

# get_img()
# print(cv_img)

def manip():
    #cv_image = cv.cvtColor(np.array(photo), cv.COLOR_RGB2BGR)
    if techniq.get() == "Select Technique":
        messagebox.showinfo("Technique Error", "Please select one of the techniques to manipulate e.g Grayscale.")
    elif techniq.get() == "Rotate":
        # cv.namedWindow("Rotate", cv.WINDOW_AUTOSIZE)
        # cv_imgs = cv.resize(cv_img, (960, 540))
        rotate = cv.rotate(cv_img, cv.ROTATE_90_CLOCKWISE)
        cv.imshow("Rotate", cv_img)
    elif techniq.get() == "Grayscale":
        grayscale = cv.cvtColor(cv_img, cv.COLOR_BGR2GRAY)
        cv.imshow("Grayscale", grayscale)
    elif techniq.get() == "Sharpen":
        pass
    elif techniq.get() == "Blur":
        blur = cv.blur(cv_img, (10, 10))
        cv.imshow("Blur", blur)
    elif techniq.get() == "sketch":
        pass
mnp_btn = tkinter.Button(master=frame_4, text = "Manipulate", bg = "purple", fg="white", width=16, height=2, command=manip)
mnp_btn.pack()
packs()
window.mainloop()