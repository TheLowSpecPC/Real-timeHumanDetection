from tkinter import *
from tkinter import filedialog
import os
import threading
import detection

cwd = os.getcwd()

root = Tk()
root.geometry("700x300")
root.title("Real Time Human Detection (Made By: The Low Spec PC)")
root.iconbitmap(cwd+"/icon.ico")
root.config(bg="gray")

def img_input():
        with open(cwd + "/Info/image.txt", "w") as a1:
            a = filedialog.askopenfilename(initialdir="C:/", title="Select a Image")
            a1.write(a)
            a1.close()

def vid_input():
        with open(cwd + "/Info/video.txt", "w") as b1:
            b = filedialog.askopenfilename(initialdir="C:/", title="Select a Video")
            b1.write(b)
            b1.close()

def camera():
    root1 = Tk()
    root1.geometry("400x100")
    root1.title("Camera Selection")
    root1.iconbitmap(cwd + "/icon.ico")
    root1.config(bg="gray")

    def cam0():
        detection.detectByCamera(0)

    def cam1():
        detection.detectByCamera(1)

    def cam2():
        detection.detectByCamera(2)

    def cam3():
        detection.detectByCamera(3)

    Label(root1, text="Choose Your Camera", font=("Raleway", 18), bg="black", fg="white", height="1").place(x=90, y=1)

    Button(root1, text="Cam 1", command=threading.Thread(target=cam0).start, width="8", height="1").place(x=20, y=50)
    Button(root1, text="Cam 2", command=threading.Thread(target=cam1).start, width="8", height="1").place(x=120, y=50)
    Button(root1, text="Cam 3", command=threading.Thread(target=cam2).start, width="8", height="1").place(x=220, y=50)
    Button(root1, text="Cam 4", command=threading.Thread(target=cam3).start, width="8", height="1").place(x=320, y=50)

    root1.mainloop()

def image():
        with open(cwd + "/Info/image.txt", "r") as c1:
            img = c1.readline()
            c1.close()
        detection.detectByPathImage(img)

def video():
    with open(cwd + "/Info/video.txt", "r") as d1:
        vid = d1.readline()
        d1.close()
    detection.detectByPathVideo(vid)

Label(root, text="Choose the medium of detection", font=("Raleway", 20), bg="black", fg="white", height="1").place(x=140, y=1)

Label(root, text="Camera", font=("Raleway", 18), bg="black", fg="white", height="1").place(x=230, y=60)
Button(root, text="Start", command=camera, width="10", height="1").place(x=350, y=65)

Label(root, text="Image", font=("Raleway", 18), bg="black", fg="white", height="1").place(x=200, y=110)
Button(root, text="Select a Image", command= img_input, width="12", height="1").place(x=290, y=115)
Button(root, text="Start", command=threading.Thread(target=image).start, width="10", height="1").place(x=400, y=115)

Label(root, text="Video", font=("Raleway", 18), bg="black", fg="white", height="1").place(x=205, y=160)
Button(root, text="Select a Video", command= vid_input, width="12", height="1").place(x=290, y=165)
Button(root, text="Start", command=threading.Thread(target=video).start, width="10", height="1").place(x=400, y=165)

root.mainloop()