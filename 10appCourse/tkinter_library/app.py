from sqlite3.dbapi2 import Cache
from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index = lb1.curselection()[0]
        selected_tuple = lb1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass


def view_command():
    lb1.delete(0,END)
    for row in backend.view():
        lb1.insert(END, row)

def search_command():
    lb1.delete(0,END)
    for row in backend.search(e1_val.get(), e2_val.get(), e3_val.get(), e4_val.get()):
        lb1.insert(END, row)

def add_command():
    backend.insert(e1_val.get(), e2_val.get(), e3_val.get(), e4_val.get())
    lb1.delete(0,END)
    lb1.insert(END, (e1_val.get(), e2_val.get(), e3_val.get(), e4_val.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0], e1_val.get(), e2_val.get(), e3_val.get(), e4_val.get())
    print(selected_tuple[0], e1_val.get(), e2_val.get(), e3_val.get(), e4_val.get())

window=Tk()

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)


#var for value from e1 field
e1_val=StringVar()
e1=Entry(window, textvariable=e1_val)
e1.grid(row=0,column=1)
#var for value from e1 field
e2_val=StringVar()
e2=Entry(window, textvariable=e2_val)
e2.grid(row=0,column=3)
#var for value from e1 field
e3_val=StringVar()
e3=Entry(window, textvariable=e3_val)
e3.grid(row=1,column=1)
#var for value from e1 field
e4_val=StringVar()
e4=Entry(window, textvariable=e4_val)
e4.grid(row=1,column=3)


lb1=Listbox(window, height=11, width=35)
lb1.grid(row=2,column=0,columnspan=2,rowspan=6)

lb1.bind('<<ListboxSelect>>', get_selected_row)

#sb1=Scrollbar(window)
#sb1.grid(row=2,columns=2, rowspan=4)

#lb1.configure(yscrollcommand=sb1.set)
#sb1.configure(command=lb1.yview)

b1=Button(window, text="View all",width=10, command=view_command)
b1.grid(row=2,column=3)

b2=Button(window, text="Search",width=10, command=search_command)
b2.grid(row=3,column=3)

b3=Button(window, text="Add",width=10, command=add_command)
b3.grid(row=4,column=3)

b4=Button(window, text="Update",width=10, command=update_command)
b4.grid(row=5,column=3)

b5=Button(window, text="Delete",width=10, command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window, text="Close",width=10, command=window.destroy)
b6.grid(row=7,column=3)


#keeps window open
window.mainloop()
