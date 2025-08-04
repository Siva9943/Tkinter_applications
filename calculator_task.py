from tkinter import *
from tkinter import messagebox

cal = Tk()
cal.geometry('500x500')
cal.title('Calculator')
cal.configure(bg='black')
def calculate(action):
    try:
        a = int(num1.get())
        b = int(num2.get())

        if action == 'add':
            result = a + b
        elif action == 'subtract':
            result = a - b
        elif action == 'multiply':
            result = a * b
        elif action == 'divide':
            result = a / b
        messagebox.showinfo('Result', f'Total value: {result}')
    except ValueError as e:
        messagebox.showerror('Error', e)
    except ZeroDivisionError as zero:
        messagebox.showerror('Error', zero)


num1 = StringVar()
num2 = StringVar()

Label(cal, text='Enter the first number:', font=('calibri', 18), fg='white', bg='black').place(x=30, y=50)
Entry(cal, textvariable=num1, font=('calibri', 18), bg='lightyellow', width=18).place(x=300, y=50)
Label(cal, text='Enter the second number:', font=('calibri', 18), fg='white', bg='black').place(x=30, y=120)
Entry(cal, textvariable=num2, font=('calibri', 18), bg='lightyellow', width=18).place(x=300, y=120)

Button(cal, text='+', font=('calibri', 18),fg='white', bg='black', command=lambda: calculate('add')).place(x=30, y=200)
Button(cal, text='-', font=('calibri', 18),fg='white', bg='black', command=lambda: calculate('subtract')).place(x=100, y=200)
Button(cal, text='*', font=('calibri', 18), fg='white',bg='black', command=lambda: calculate('multiply')).place(x=170, y=200)
Button(cal, text='/', font=('calibri', 18),fg='white', bg='black', command=lambda: calculate('divide')).place(x=240, y=200)
Button(cal, text='C', font=('calibri', 18),fg='white', bg='red', command=lambda: (num1.set(''), num2.set(''))).place(x=310, y=200)

cal.mainloop()
