from tkinter import *

newWindow1 = Tk()
newWindow1.geometry("600x600")
newWindow1.configure(bg="white")

my_list1 = [
    "This is a sample software to manage criminal records using",
    "mySQL and Python",
    "This software is written by SSU STUDENT",
    "Who is a student of SRI SRI UNIVERSITY",
    "\n",
    "\n",
    "\n",
    "SATYAMEV JAYATE",
]
txt1_output = Text(newWindow1, height=25, width=60)
txt1_output.pack(pady=30)
for item in my_list1:
    txt1_output.insert(END, item + "\n")
newWindow1.mainloop()
