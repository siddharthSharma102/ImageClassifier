import tkinter
from tkinter import Entry, Label

master = tkinter.Tk()
master.geometry('600x600')
Label(master, text = 'First Name').grid(row = 0)
Label(master, text = 'Second Name').grid(row = 1)
e1 = Entry(master).grid(row = 0, column = 1)
e2 = Entry(master).grid(row = 1, column = 1)
print(e1.get())



master.mainloop()