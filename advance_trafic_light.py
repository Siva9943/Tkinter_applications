from tkinter import *
import tkinter.messagebox as messagebox

obj = Tk()
obj.geometry("600x500")
obj.title("Advance Traffic Light")
obj.config(bg="lightblue")

switch_text = StringVar()
switch_text.set("Manual Mode")
timer_label = Label(obj, text="", font=("Arial", 16, "bold"), bg="lightblue")
timer_label.place(x=330, y=470)
phase = 0  
time_left = 25
run = False
c1 = Canvas(obj, width=130, height=130, bg="black"); c1.place(x=150, y=50)
c2 = Canvas(obj, width=130, height=130, bg="black"); c2.place(x=150, y=185)
c3 = Canvas(obj, width=130, height=130, bg="black"); c3.place(x=150, y=320)
c4 = Canvas(obj, width=130, height=130, bg="black"); c4.place(x=300, y=50)
c5 = Canvas(obj, width=130, height=130, bg="black"); c5.place(x=300, y=185)
c6 = Canvas(obj, width=130, height=130, bg="black"); c6.place(x=300, y=320)
c7 = Canvas(obj, width=130, height=130, bg="black"); c7.place(x=450, y=50)
c8 = Canvas(obj, width=130, height=130, bg="black"); c8.place(x=450, y=185)
c9 = Canvas(obj, width=130, height=130, bg="black"); c9.place(x=450, y=320)

canvas_list = [c1, c2, c3, c4, c5, c6, c7, c8, c9]

def menual(data):
    try:
        for c in canvas_list:
            c.delete("all")

        if data == "red":
            c1.create_oval(20, 20, 110, 110, outline='white', fill='red', width=2)
            c5.create_oval(20, 20, 110, 110, outline='white', fill='yellow', width=2)
            c9.create_oval(20, 20, 110, 110, outline='white', fill='green', width=2)

        elif data == "yellow":
            c2.create_oval(20, 20, 110, 110, outline='white', fill='yellow', width=2)
            c7.create_oval(20, 20, 110, 110, outline='white', fill='red', width=2)
            c6.create_oval(20, 20, 110, 110, outline='white', fill='green', width=2)

        elif data == "green":
            c3.create_oval(20, 20, 110, 110, outline='white', fill='green', width=2)
            c5.create_oval(20, 20, 110, 110, outline='white', fill='yellow', width=2)
            c7.create_oval(20, 20, 110, 110, outline='white', fill='red', width=2)
    except Exception as e:
        messagebox.showerror("Error", f"Error is {e}")

def switch():
    global run, time_left, phase
    if switch_text.get() == "Manual Mode":
        switch_text.set("Automatic Mode")
        red_button.config(state='disabled')
        yellow_button.config(state='disabled')
        green_button.config(state='disabled')
        run = True
        time_left = 25
        phase = 0
        automatic_cycle()
    else:
        switch_text.set("Manual Mode")
        red_button.config(state='normal')
        yellow_button.config(state='normal')
        green_button.config(state='normal')
        run = False
        timer_label.config(text="")
        for c in canvas_list:
            c.delete("all")

def automatic_cycle():
    global time_left, phase

    if not run:
        return

    for c in canvas_list:
        c.delete("all")

    if phase == 0:
        menual("red")
    elif phase == 1:
        menual("yellow")
    elif phase == 2:
        menual("green")
    timer_label.config(font=("Arial", 25, "bold"), text=time_left)
    time_left -= 1

    if time_left < 0:
        phase = (phase + 1) % 3 
        time_left = 25

    obj.after(1000, automatic_cycle)

red_button = Button(obj, text="Turn on Red", bg="red", width=12, height=2, command=lambda: menual("red"))
red_button.place(x=20, y=70)

yellow_button = Button(obj, text="Turn on Yellow", bg="yellow", width=12, height=2, command=lambda: menual("yellow"))
yellow_button.place(x=20, y=200)

green_button = Button(obj, text="Turn on Green", bg="green", width=12, height=2, command=lambda: menual("green"))
green_button.place(x=20, y=330)

Button(obj, textvariable=switch_text, bg="blue", fg="white", width=17, height=3, padx=30, command=switch).place(x=180, y=520)

obj.mainloop()
