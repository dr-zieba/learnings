from tkinter import *

window = Tk()
window.geometry("350x100+300+300")
window.iconbitmap('favicon.ico')
window.title("Converter")

def convert():
    print(e1_val.get())

    grams = float(e1_val.get()) * 1000
    t1.delete("1.0",END)
    t1.insert(END, "{0:.2f}".format(grams))

    pounds = float(e1_val.get()) * 2.20
    t2.delete("1.0",END)
    t2.insert(END, "{0:.2f}".format(pounds))

    ounce = float(e1_val.get()) * 35.274
    t3.delete("1.0",END)
    t3.insert(END, "{0:.2f}".format(ounce))

def clear():
    t1.delete("1.0",END)
    t2.delete("1.0",END)
    t3.delete("1.0",END)

l1 = Label(window, text="Kg")
l1.grid(row=0, column=0)

e1_val = StringVar()
e1 = Entry(window, textvariable=e1_val)
e1.grid(row=0, column=1)

b1 = Button(window, text="Convert", command=convert)
b1.grid(row=0, column=2)

b2 = Button(window, text="Clear", command=clear)
b2.grid(row=0, column=3)

t1 = Text(window, height=2, width=10)
t1.grid(row=1, column=0)

t2 = Text(window, height=2, width=10)
t2.grid(row=1, column=1)

t3 = Text(window, height=2, width=10)
t3.grid(row=1, column=2)

window.mainloop()
