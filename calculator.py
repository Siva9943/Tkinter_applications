from tkinter import *

# Create main window
root = Tk()
root.title("Basic Calculator")
root.geometry("300x400")
root.configure(bg='lightgray')

expression = ""

# Function to update expression in text entry box
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total  # allow further operations
    except:
        equation.set("Error")
        expression = ""

# Function to clear the entry box
def clear():
    global expression
    expression = ""
    equation.set("")

# StringVar() is the variable class
equation = StringVar()

# Entry widget to show the expression
entry = Entry(root, textvariable=equation, font=('Arial', 20), bd=10, relief=RIDGE, justify='right')
entry.grid(columnspan=4, ipadx=2, ipady=3, pady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        btn = Button(root, text=text, fg='white', bg='green', font=('Arial', 16), height=2, width=6, command=equalpress)
    elif text == 'C':
        btn = Button(root, text=text, fg='white', bg='red', font=('Arial', 16), height=2, width=6, command=clear)
    else:
        btn = Button(root, text=text, font=('Arial', 16), height=2, width=6, command=lambda t=text: press(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
