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

        else:
            try:
                value = eval(screen.get())
                scvalue.set(value)
                screen.update()
            except:
                ZeroDivisionError
                tmsg.showinfo("Error","Can't Divide by Zero")
                scvalue.set("Error")
                screen.update()


    elif text == "C" or text == "AC":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
# while True:
#     time = time.asctime()



# def clock():
#     while True:
#         print(datetime.datetime.now().strftime("%H:%M:%S"), end="\r")
#         time.sleep(1)
# clock = time.asctime()
# while True:
#     time.sleep(1)

lb = Label(text=time.asctime())
lb.pack(side=BOTTOM,fill=X)

scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvariable=scvalue,font="lucida 40 bold")
screen.pack(padx=10,pady=10)

f = Frame(root,bg="#979797")
f.pack()

b = Button(f,text="7",padx=15,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=12,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="8",padx=15,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=12,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="9",padx=15,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=12,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="C",padx=15,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=13,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="AC",padx=20,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=8,pady=10)
b.bind("<Button-1>",click)

f = Frame(root,bg="#979797")
f.pack()

b = Button(f,text="4",padx=15,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=12,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="5",padx=16,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=12,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="6",padx=16,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=12,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="*",padx=18,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=13,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="-",padx=15,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=4,pady=10)
b.bind("<Button-1>",click)

f = Frame(root,bg="#979797")
f.pack()

b = Button(f,text="1",padx=15,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=12,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="2",padx=15,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=12,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="3",padx=15,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="/",padx=18,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=12,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="+",padx=15,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=8,pady=10)
b.bind("<Button-1>",click)

f = Frame(root,bg="#979797")
f.pack()

b = Button(f,text=".",padx=18,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="0",padx=15,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="00",padx=10,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="=",padx=15,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=18,pady=10)
b.bind("<Button-1>",click)

b = Button(f,text="%",padx=15,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=13,pady=10)
b.bind("<Button-1>",click)

root.mainloop()
