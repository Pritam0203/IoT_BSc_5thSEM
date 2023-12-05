import mysql.connector
import tkinter  as tk
from tkinter import *
record_window = tk.Tk()
record_window.title("NAME                                                   FATHER'S NAME                           MOTHER'S NAME                   CASE_NUMBER             CRIME NAME         DETAILS                ")
record_window.geometry("1000x500")

my_connect = mysql.connector.connect(
  host="localhost",#server name
  user="rudra",#username
  password="Rudra750#z1x2",#password:in my case there is no password so i left blank
  database="crm"#database name
)
my_conn = my_connect.cursor()
my_conn.execute("SELECT * FROM crm")
i=0
for student in my_conn:
    for j in range(len(student)):
        e = Entry(record_window, width=20, fg='red',bg='black')
        e.grid(row=i, column=j)
        e.insert(END, student[j])
    i=i+1
record_window.mainloop()