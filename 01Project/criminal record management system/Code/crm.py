from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image
import mysql.connector
import os

root = Tk()
root.geometry("1200x800")
root.title("CRIME RECORD MANAGEMENT SYSTEM")
root.config(bg="white")

menubar = Menu(root)


def search():
    os.system("python search.py")


def about():
    os.system("python demo.py")


def demo():
    global w
    c = w.get()
    global w1
    d = w1.get()
    print(c)
    global w2
    e = w2.get()
    global w3
    f = w3.get()
    global w4
    g = w4.get()
    global w5
    h = w5.get()
    my_conn = mysql.connector.connect(
        host="localhost", user="root", password="toor", database="crm"
    )
    print(my_conn)
    cursor = my_conn.cursor()
    cursor.execute("use crm")
    sql = "insert into crm(name,crime,place,caseno,policestation,details)values(%s,%s,%s,%s,%s,%s)"
    data = (c, d, e, f, g, h)
    cursor.execute(sql, data)
    my_conn.commit()
    messagebox.showinfo("INFORMATION", "ENTRY DONE")


def exit11():
    root.quit()


def openNewWindow():
    newWindow = Toplevel(root)
    newWindow.title("SAFETY TIPS")
    newWindow.geometry("600x600")
    newWindow.configure(bg="white")
    my_list = [
        "Share a secret code word",
        "You and your parents should agree on a code",
        "that is easy for you to remember to use in emergency",
        "Stay away from strangers",
        "Grownups should NOT ask kids to do things that other adults can do for them.",
        "If someone follows you on foot or in a car, STAY AWAY.",
        "If you think you are not secure",
        "Call us immediately +91 8018295791 ",
        "\n",
        "\n",
        "\n",
        "SATYAMEV JAYATE",
    ]
    txt_output = Text(newWindow, height=25, width=60)
    txt_output.pack(pady=30)
    ww = Label(
        newWindow,
        text="                   SSU CRIME MANAGEMENT SYSTEM COPYRIGHT 2023",
        height=1,
        bg="white",
        fg="black",
    ).place(x=40, y=550)
    for item in my_list:
        txt_output.insert(END, item + "\n")
        pass


def crime():
    os.system("python demo1.py")


menubar.add_command(label="CRIME LIST", command=crime)
menubar.add_command(label="TIPS FROM US", command=openNewWindow)
menubar.add_command(label="ABOUT SOFTWARE", command=about)
menubar.add_command(label="SEARCH FOR A CRIMINAL DATA", command=search)
menubar.add_command(label="EXIT", command=exit11)
root.config(menu=menubar)
canvas_widget = Canvas(root, width=1200, height=800)
canvas_widget.pack()
img = ImageTk.PhotoImage(Image.open("16.jpg"))
canvas_widget.create_image(550, 350, image=img)
l = Label(root, text="CRIMINAL NAME", fg="black", bg="red", height=1, width=25)
canvas_widget.create_window(200, 30, window=l)
w = Entry(root, width=25)
canvas_widget.create_window(200, 60, window=w)
l1 = Label(root, text="FATHER'S NAME", fg="black", bg="white", height=1, width=25)
canvas_widget.create_window(200, 90, window=l1)
w1 = Entry(root, width=25)
canvas_widget.create_window(200, 120, window=w1)
l2 = Label(root, text="MOTHER'S NAME", fg="white", bg="green", height=1, width=25)
canvas_widget.create_window(200, 150, window=l2)
w2 = Entry(root, width=25)
canvas_widget.create_window(200, 180, window=w2)
b = Button(root, text="SUBMIT", height=2, width=10, bg="red", fg="white", command=demo)
l3 = Label(root, text="CASE NUMBER", height=1, width=25, bg="red", fg="black")
canvas_widget.create_window(450, 30, window=l3)
w3 = Entry(root, width=25)
canvas_widget.create_window(450, 60, window=w3)
l4 = Label(root, text="CRIME NAME", bg="white", fg="black", height=1, width=25)
canvas_widget.create_window(450, 90, window=l4)
w4 = Entry(root, width=25)
canvas_widget.create_window(450, 120, window=w4)
l5 = Label(root, text="CRIME DETAILS", fg="white", bg="green", height=1, width=25)
canvas_widget.create_window(450, 150, window=l5)
w5 = Entry(root, width=25)
canvas_widget.create_window(450, 180, window=w5)
canvas_widget.create_window(350, 230, window=b)
mainloop()
