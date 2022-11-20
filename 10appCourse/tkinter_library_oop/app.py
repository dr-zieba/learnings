from sqlite3.dbapi2 import Cache
from tkinter import *
from backend import Database


class Window(object):
    def __init__(self):
        self.database = Database()
        window=Tk()

        self.l1=Label(window,text="Title")
        self.l1.grid(row=0,column=0)

        self.l2=Label(window,text="Author")
        self.l2.grid(row=0,column=2)

        self.l3=Label(window,text="Year")
        self.l3.grid(row=1,column=0)

        self.l4=Label(window,text="ISBN")
        self.l4.grid(row=1,column=2)


        #var for value from e1 field
        self.e1_val=StringVar()
        self.e1=Entry(window, textvariable=self.e1_val)
        self.e1.grid(row=0,column=1)
        #var for value from e1 field
        self.e2_val=StringVar()
        self.e2=Entry(window, textvariable=self.e2_val)
        self.e2.grid(row=0,column=3)
        #var for value from e1 field
        self.e3_val=StringVar()
        self.e3=Entry(window, textvariable=self.e3_val)
        self.e3.grid(row=1,column=1)
        #var for value from e1 field
        self.e4_val=StringVar()
        self.e4=Entry(window, textvariable=self.e4_val)
        self.e4.grid(row=1,column=3)


        self.lb1=Listbox(window, height=11, width=35)
        self.lb1.grid(row=2,column=0,columnspan=2,rowspan=6)

        self.lb1.bind('<<ListboxSelect>>', self.get_selected_row)

        #sb1=Scrollbar(window)
        #sb1.grid(row=2,columns=2, rowspan=4)

        #lb1.configure(yscrollcommand=sb1.set)
        #sb1.configure(command=lb1.yview)

        b1=Button(window, text="View all",width=10, command=self.view_command)
        b1.grid(row=2,column=3)

        b2=Button(window, text="Search",width=10, command=self.search_command)
        b2.grid(row=3,column=3)

        b3=Button(window, text="Add",width=10, command=self.add_command)
        b3.grid(row=4,column=3)

        b4=Button(window, text="Update",width=10, command=self.update_command)
        b4.grid(row=5,column=3)

        b5=Button(window, text="Delete",width=10, command=self.delete_command)
        b5.grid(row=6,column=3)

        b6=Button(window, text="Close",width=10, command=window.destroy)
        b6.grid(row=7,column=3)


        #keeps window open
        window.mainloop()

    def get_selected_row(self, event):
        try:
            global selected_tuple
            index = self.lb1.curselection()[0]
            selected_tuple = self.lb1.get(index)
            self.e1.delete(0, END)
            self.e1.insert(END, selected_tuple[1])
            self.e2.delete(0, END)
            self.e2.insert(END, selected_tuple[2])
            self.e3.delete(0, END)
            self.e3.insert(END, selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(END, selected_tuple[4])
        except IndexError:
            pass


    def view_command(self):
        self.lb1.delete(0,END)
        for row in self.database.view():
            self.lb1.insert(END, row)

    def search_command(self):
        self.lb1.delete(0,END)
        row = self.database.search(self.e1_val.get(), self.e2_val.get(), self.e3_val.get(), self.e4_val.get())
        self.lb1.insert(END, row)

    def add_command(self):
        self.database.insert(self.e1_val.get(), self.e2_val.get(), self.e3_val.get(), self.e4_val.get())
        self.lb1.delete(0,END)
        self.lb1.insert(END, (self.e1_val.get(), self.e2_val.get(), self.e3_val.get(), self.e4_val.get()))

    def delete_command(self):
        self.database.delete(selected_tuple[0])

    def update_command(self):
        self.database.update(selected_tuple[0], self.e1_val.get(), self.e2_val.get(), self.e3_val.get(), self.e4_val.get())
        print(selected_tuple[0], self.e1_val.get(), self.e2_val.get(), self.e3_val.get(), self.e4_val.get())

 
if __name__=='__main__':
    window = Window()

