from tkinter import*

class notebook():
    def __init__(self,master):
        
        menu=Menu(master)
        master.config(menu=menu)

        file_menu=Menu(menu)
        menu.add_cascade(label="File",menu=file_menu)

        file_menu.add_command(label="Open",command=self.odpri)
        file_menu.add_command(label="Save",command=self.shrani)
        file_menu.add_command(label="Exit",command=master.destroy)

        
        self.text=Text(root,height=40,width=50)
        self.text.pack()

    def odpri(self):
        f=filedialog.askopenfilename()
        print(f)
        print(type(f))

        with open(f,"r")as g:
            self.text.insert(END,g.read())

    def shrani(self):
        f = filedialog.asksaveasfile(defaultextension=".txt")
        f.write(self.text.get(1.0, END))
        f.close()
   

root=Tk()
app=notebook(root)
root.mainloop()
