from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

import os


def sus():
    global e
    global e1
    s = e.get()
    x = e1.get()
    if (s == "ssu") and (x == "ssu1234"):
        os.system("python crm.py")

    else:
        messagebox.showinfo("WARNING", "PROJECT ACCESS DENIED ")


def exit():
    root.quit()


root = Tk()
root.geometry("1000x600")
root.title("login")
canvas_widget = Canvas(root, height=1000, width=1000)
canvas_widget.pack()
img = ImageTk.PhotoImage(Image.open("13.jpg"))
canvas_widget.create_image(500, 300, image=img)
w = Label(root, text="PROJECT LOGIN", bg="black", fg="white")
w1 = Label(root, text="ENTER ID", bg="black", fg="white")
canvas_widget.create_window(200, 230, window=w1)
canvas_widget.create_window(200, 200, window=w)
e = Entry(root, width=20)
w2 = Label(root, text="ENTER PASSWORD", fg="white", bg="black")
canvas_widget.create_window(200, 290, window=w2)
canvas_widget.create_window(200, 260, window=e)
e1 = Entry(root, show="*", width=20)
canvas_widget.create_window(200, 320, window=e1)
b1 = Button(root, text="login", bg="black", fg="white", command=sus)
canvas_widget.create_window(200, 370, window=b1)
mainloop()
