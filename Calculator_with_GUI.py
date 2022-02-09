import time
from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title("Calculator - By Deveesh")
root.iconbitmap("Dtafalonso-Android-Lollipop-Calculator.ico")
root.geometry("420x600")
root.configure(bg="#979797")
root.maxsize(400,500)
root.minsize(400,500)

def click(event):
    global scvalue
    text=event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
            value = eval(screen.get())
            scvalue.set(value)
            screen.update()

        else:
            try:
                value = eval(screen.get())
                scvalue.set(value)
                screen.update()
            except:
                ZeroDivisionError
                tmsg.showinfo("Error","Give a right Command!")
                scvalue.set("Error")
                screen.update()
                time.sleep(1)
                scvalue.set('')
                screen.update()

    elif text == "C" or text == "AC":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

lb = Label(text=time.asctime(),relief=GROOVE)
lb.pack(side=BOTTOM,fill=X)

scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvariable=scvalue,font="lucida 40 bold")
screen.pack(padx=10,pady=10)

button_list = (7,8,9,'C','AC',4,5,6,'*','-',1,2,3,'/','+','.',0,'00','=','%')
for i in button_list:
    if i == 7 or i == 4 or i == 1 or i == '.':
        f = Frame(root, bg="#979797",relief=SUNKEN)
        f.pack()
    b = Button(f, text=str(i), padx=16, pady=10, font="lucida 15 bold",relief=GROOVE)
    b.pack(side=LEFT, padx=12, pady=10)
    b.bind("<Button-1>", click)

root.mainloop()
