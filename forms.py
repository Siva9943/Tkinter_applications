from tkinter import *
from tkinter import messagebox

obj = Tk()
obj.geometry('400x400')
obj.title('Sample Form')
obj.configure(bg='lightblue')

def add():
    a = num1.get()
    b = num2.get()
    c = a + b
    messagebox.showinfo('Result', 'Total value: ' + str(c))

Label(obj, text='Enter the first num :', font=('calibri', 18), bg='aqua').place(x=20, y=30)
Label(obj, text='Enter the second num :', font=('calibri', 18), bg='aqua').place(x=20, y=100)

num1 = IntVar()
num2 = IntVar()

Entry(obj, textvariable=num1, font=('calibri', 18)).place(x=170, y=30)
Entry(obj, textvariable=num2, font=('calibri', 18)).place(x=170, y=100)

Button(obj, text='Add Value', font=('calibri', 15), bg='black', fg='white', width=12, height=1, command=add).place(x=140, y=250)

obj.mainloop()
