from tkinter import *

window=Tk()
def dollar_to_rupees():
    print(e1_value.get())
    dollar=float(e1_value.get())/76.4
    euros=float(e1_value.get())/80
    rial=float(e1_value.get())/18
    t1.insert(END,dollar)
    t2.insert(END,euros)
    t3.insert(END,rial)
b1=Button(window,text="press to convert",command=dollar_to_rupees)
b1.grid(row=0,column=1)

e=Label(window,text="rupees")
e.grid(row=0,column=3)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=2)

t1=Text(window,height=1,width=10)
t1.grid(row=3,column=0)

e1=Label(window,text="$")
e1.grid(row=3,column=1)

t2=Text(window,height=1,width=10)
t2.grid(row=3,column=2)

e2=Label(window,text="euro")
e2.grid(row=3,column=3)

t3=Text(window,height=1,width=10)
t3.grid(row=3,column=4)

e3=Label(window,text="rial")
e3.grid(row=3,column=5)

window.mainloop()
