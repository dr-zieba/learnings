from tkinter import *
from backend import Database

database = Database("database.db")

class Fronend(object):

    def __init__(self, window, title):
        self.window = window
        self.window.title(title)

        l1 = Label(window,text="Title")
        l1.grid(row=0,column=0)

        self.e1Var = StringVar()
        self.e1 = Entry(window,textvariable=self.e1Var)
        self.e1.grid(row=0,column=1)

        l2 = Label(window,text="Author")
        l2.grid(row=0,column=2)

        self.e2Var = StringVar()
        self.e2 = Entry(window,textvariable=self.e2Var)
        self.e2.grid(row=0,column=3)

        l3 = Label(window,text="Year")
        l3.grid(row=1,column=0)

        self.e3Var = StringVar()
        self.e3 = Entry(window,textvariable=self.e3Var)
        self.e3.grid(row=1,column=1)

        l4 = Label(window,text="ISBN")
        l4.grid(row=1,column=2)

        self.e4Var = StringVar()
        self.e4 = Entry(window,textvariable=self.e4Var)
        self.e4.grid(row=1,column=3)

        self.lb = Listbox(window,height=11,width=35)
        self.lb.grid(row=2,column=0,columnspan=2,rowspan=8)

        scroll = Scrollbar(window)
        scroll.grid(row=2,column=2,rowspan=6)

        self.lb.configure(yscrollcommand=scroll.set)
        scroll.configure(command=self.lb.yview)

        self.lb.bind('<<ListboxSelect>>',self.get_index)

        b1 = Button(window, text="Add Entry",width=12, command=self.add_command)
        b1.grid(column=3,row=2)

        b2 = Button(window, text="Show All",width=12, command=self.showAll_command)
        b2.grid(column=3,row=3)

        b3 = Button(window, text="Search",width=12, command=self.search_command)
        b3.grid(column=3,row=4)

        b4 = Button(window, text="Delete",width=12, command=self.delete_command)
        b4.grid(column=3,row=5)

        b5 = Button(window, text="Update",width=12, command=self.update_command)
        b5.grid(column=3,row=6)

        b6 = Button(window, text="Close",width=12, command=self.close_command)
        b6.grid(column=3,row=7)

        b7 = Button(window, text="Clear",width=12, command=self.clear_command)
        b7.grid(column=3,row=8)


    def get_index(self, event):
        index = self.lb.curselection()[0]
        self.selected_row = self.lb.get(index)
        self.e1.delete(0,END)
        self.e1.insert(END, self.selected_row[1])
        self.e2.delete(0,END)
        self.e2.insert(END, self.selected_row[2])
        self.e3.delete(0,END)
        self.e3.insert(END, self.selected_row[3])
        self.e4.delete(0,END)
        self.e4.insert(END, self.selected_row[4])

    def add_command(self):
        database.add(self.e1Var.get(),self.e2Var.get(),self.e3Var.get(),self.e4Var.get())
        self.lb.delete(0,END)
        self.lb.insert(END,(self.e1Var.get(),self.e2Var.get(),self.e3Var.get(),self.e4Var.get()))

    def showAll_command(self):
        self.lb.delete(0,END)
        for row in database.showAll():
            self.lb.insert(END, row)

    def search_command(self):
        self.lb.delete(0,END)
        for row in database.search(self.e1Var.get(),self.e2Var.get(),self.e3Var.get(),self.e4Var.get()):
            self.lb.insert(END,row)

    def delete_command(self):
        database.delete(self.selected_row[0])

    def update_command(self):
        database.update(self.e1Var.get(),self.e2Var.get(),self.e3Var.get(),self.e4Var.get(),self.selected_row[0])
        self.lb.delete(0,END)
        for row in database.search(self.e1Var.get(),self.e2Var.get(),self.e3Var.get(),self.e4Var.get()):
            self.lb.insert(END,row)


    def close_command(self):
        window.destroy()

    def clear_command(self):
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.e4.delete(0,END)
        self.lb.delete(0,END)

window = Tk()
Fronend(window, "Biblioteka")
window.mainloop()
