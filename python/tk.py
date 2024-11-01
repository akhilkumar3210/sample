import tkinter
win=tkinter.Tk()
win.title("demo")
win.configure(bg='silver')
win.minsize(400,400)
win.maxsize(800,800)

def submit():
    print(e1.get())
    l3.config(text=e1.get())
    f=open("demo3",'a')
    f.write(e1.get())
    if var1.get()==1:
        print('Male')
    else:
        print('Female')


l1=tkinter.Label(win,text='Sample Win',bg='silver')
l1.place(x=165,y=25)
l2=tkinter.Label(win,text='Name :',bg='silver')
l2.place(x=65,y=55)
e1=tkinter.Entry(win)
e1.place(x=120,y=55)
l4=tkinter.Label(win,text='Gender :',bg='silver')
l4.place(x=65,y=95)
var1=tkinter.IntVar()
r1=tkinter.Radiobutton(win,text='Male',variable=var1,value=1,bg='silver')
r1.place(x=145,y=95)
r2=tkinter.Radiobutton(win,text='Female',variable=var1,value=2,bg='silver')
r2.place(x=245,y=95)
btn1=tkinter.Button(win,text="Submit",bg='white',fg='gold',activebackground='white',activeforeground='black',padx=5,pady=5,command=submit)
# btn1.pack()
btn1.place(x=160,y=170)
l3=tkinter.Label(win)
l3.place(x=120,y=240)

win.mainloop()