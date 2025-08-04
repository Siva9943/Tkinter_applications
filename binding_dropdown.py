from tkinter import *
from tkinter import ttk, messagebox
obj= Tk()
obj.geometry('400x400')
obj.title('Binding Dropdown Example')
obj.configure(bg='Black')
def get_values(selected):
    menu2.set_menu(*option2.get(selected)
        )
Label(obj,text="select Your Distict",font=('calibri',15),bg='lightblue').place(x=20,y=30)
option1=['Thiruvannamalai','chengalpattu','gingee','tirunelveli','madurai']
values1=StringVar()
menu1=ttk.OptionMenu(obj,values1,'--------select----------',option1,command=get_values)
menu1.place(x=180,y=30)

Label(obj,text='Select the Distict' ,font=('calibri',15),bg='lightblue').place(x=20,y=150)
option2={
    'Thiruvannamalai' : ['keekalur','mekkalur','valithalakulam','kilpennathur','thallapadi'],
    'chengalpattu' : ['kattakulathur','tambaram','tambaram sanitorium','crompet','pallavaram'],
    'gingee': ['avalur','fort'],
    'tirunelveli':['palayakottai','yarka'],
    'madurai':['minachi kovil','madurai railway'],
}
values2=StringVar()
menu2=ttk.OptionMenu(obj,values2,"------------select-------------")
obj.mainloop()
