from tkinter import*

class drawing():
    def __init__(self,master):
        self.tocka=None

        self.canvas=Canvas(master,width=300,height=300)
        self.canvas.grid(row=0,column=0)

        self.canvas.bind("<B1-Motion>",self.crta)
        self.canvas.bind("<Button-1>",self.zacni)

        menu=Menu(master)
        master.config(menu=menu)
        menu.add_command(label="Finish",command=master.destroy)
        menu.add_command(label="Clean",command=self.pocisti)

    def crta(self,event):
        if self.tocka is not None:
            (x,y)=self.tocka
            self.canvas.create_line(x,y,event.x,event.y)
        self.tocka=(event.x,event.y)

    def zacni(self,event):
        self.tocka=(event.x,event.y)

    def pocisti(self):
        self.tocka=None
        self.canvas.delete(ALL)

root=Tk()
app=drawing(root)
root.mainloop()
