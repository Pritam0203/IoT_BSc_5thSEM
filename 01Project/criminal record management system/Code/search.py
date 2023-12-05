from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector


def rudra():
    my_connect = mysql.connector.connect(
        host="localhost",  # server name
        user="root",  # username
        password="toor",  # password:in my case there is no password so i left blank
        database="crm",  # database name
    )
    mycon = my_connect.cursor()
    global e1
    a = e1.get()
    print(a)
    sql = """select * from crm where name=%s"""
    data_tuple = [a]
    mycon.execute(sql, data_tuple)
    record_window = tk.Tk()
    record_window.geometry("900x900")
    record_window.title(
        "     CRIMINAL NAME    FATHER'S NAME    MOTHER'S NAME                 CASENUM             CRIMENAME              DETAILS   "
    )
    i = 0

    for student in mycon:
        for j in range(len(student)):
            e = Entry(record_window, width=20, fg="red", bg="black")
            e.grid(row=i, column=j)
            e.insert(END, student[j])
        i = i + 1
    record_window.mainloop()


root = Tk()
root.geometry("608x405")
root.title("SEARCH FOR A CRIMINAL")
root.eval("tk::PlaceWindow . center")
canvas_widget = Canvas(root, height=405, width=608)
canvas_widget.pack()
img = ImageTk.PhotoImage(Image.open("16.jpeg"))
canvas_widget.create_image(300, 200, image=img)
e = Label(root, text="ENTER CRIMINAL NAME   ", bg="green", fg="white")
canvas_widget.create_window(100, 40, window=e)
e1 = Entry(root, width=20)
canvas_widget.create_window(100, 70, window=e1)
b1 = Button(root, text="SUBMIT", fg="white", bg="green", command=rudra)
canvas_widget.create_window(100, 120, window=b1)
root.mainloop()
