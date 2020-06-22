from tkinter import *

class Vsota():
    def __init__(self,master):

        self.a=IntVar(master,value=0)
        self.a.trace("w",self.izracunaj)

        self.b=IntVar(master,value=0)
        self.b.trace("w",self.izracunaj)

        polje_a=Entry(master,textvariable=self.a)
        polje_a.grid(row=0,column=0)

        Label(master,text="+").grid(row=0,column=1)

        polje_b=Entry(master,textvariable=self.b)
        polje_b.grid(row=0,column=2)

        Label(master,text="=").grid(row=0,column=3)

        self.c=IntVar(master, value=self.a.get()+self.b.get())
        polje_c=Label(master,textvariable=self.c)
        polje_c.grid(row=0,column=4)

    def izracunaj(self,name,index,mode):
        try:
            self.c.set(self.a.get()+self.b.get())
        except ValueError:
            self.c.set("nedefinirano")
            






root=Tk()
app=Vsota(root)
root.mainloop()
