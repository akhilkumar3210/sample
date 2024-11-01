import mysql.connector
import tkinter
win=tkinter.Tk()
win.title("Details")
win.configure(bg='light blue')
win.minsize(400,400)
win.maxsize(800,800)
def submit():
    print(e1.get(),e2.get(),e3.get())
    g=''
    if var1.get()==1:
        g='male'
        print('Male')
    else:
        g='female'
        print('Female')
    con=mysql.connector.connect(host='localhost',user='myadmin',password='myadmin',database='admin')
    con.autocommit=True
    cur=con.cursor()
    cur.execute("insert into student (id,name,age,gender) values (%s,%s,%s,%s)",(e1.get(),e2.get(),e3.get(),g))
l0=tkinter.Label(win,text='Data Collection',bg='light blue')
l0.place(x=125,y=5)        
l1=tkinter.Label(win,text='Id :',bg='light blue')
l1.place(x=40,y=40)
e1=tkinter.Entry(win)
e1.place(x=90,y=40)
l2=tkinter.Label(win,text='Name :',bg='light blue')
l2.place(x=40,y=80)
e2=tkinter.Entry(win)
e2.place(x=90,y=80)
l3=tkinter.Label(win,text='Age :',bg='light blue')
l3.place(x=40,y=120)
e3=tkinter.Entry(win)
e3.place(x=90,y=120)
l4=tkinter.Label(win,text='Gender :',bg='light blue')
l4.place(x=40,y=160)
var1=tkinter.IntVar()
r1=tkinter.Radiobutton(win,text='Male',variable=var1,value=1)
r1.place(x=110,y=160)
r2=tkinter.Radiobutton(win,text='Female',variable=var1,value=2)
r2.place(x=190,y=160)
btn1=tkinter.Button(win,text='Submit',bg='white',fg='red',activebackground='white',activeforeground='black',padx=8,pady=8,command=submit)
btn1.place(x=150,y=230)
win.mainloop()