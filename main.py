from tkinter import *
from subprocess import call
import sys
import os
import cv2
import shutil
import threading
import detection

cwd = os.getcwd()
img = ""

root = Tk()
root.geometry("700x600")
root.title("Real Time Human Detection (Made By: The Low Spec PC)")
root.iconbitmap(cwd+"/icon.ico")
root.config(bg="gray")

def img_input():
        with open(cwd + "Info/image.txt", "w") as a1:
            a = filedialog.askopenfilename(initialdir="C:/", title="Select a Image")
            a1.write(j)
            a1.close()

def vid_input():
        with open(cwd + "Info/video.txt", "w") as b1:
            b = filedialog.askopenfilename(initialdir="C:/", title="Select a Image")
            b1.write(j)
            b1.close()

def image():
        with open(cwd + "Info/image.txt", "r") as c1:
            img = c1.read
            c1.close
        detection.detectByPathImage()

Label(root, text="Choose the medium of detection", font=("Raleway", 20), bg="black", fg="white", height="1").place(x=140, y=1)

Label(root, text="Camera", font=("Raleway", 18), bg="black", fg="white", height="1").place(x=230, y=60)
Button(root, text="Start", command=threading.Thread(target=detection.detectByCamera,args=(0,)).start, width="10", height="1").place(x=350, y=65)

Label(root, text="Image", font=("Raleway", 18), bg="black", fg="white", height="1").place(x=140, y=110)
Button(root, text="Select a Image", command= img_input, width="12", height="1").place(x=250, y=115)
Button(root, text="Start", command=threading.Thread(target=detection.detectByCamera,args=(0,)).start, width="10", height="1").place(x=350, y=65)


root.mainloop()