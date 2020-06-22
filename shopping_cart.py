from tkinter import*
class KOSARICA():
    def __init__(self, master):
        izdelek=Label(text="IZDELEK",bg="red")
        izdelek.grid(row=0,column=0)
        kolicina=Label(text="KOLIČINA",bg="red")
        kolicina.grid(row=0, column=2)
        cena=Label(text="CENA",bg="red")
        cena.grid(row=0,column=4)
        #dodatno
        poraba=Label(text="Največja poraba",bg="yellow")
        poraba.grid(row=4,column=0)

        self.izdelek=StringVar(master, value=None)
        polje_izdelek=Entry(master, textvariable=self.izdelek)
        polje_izdelek.grid(row=1,column=0)

        self.kolicina=IntVar(master, value=None)
        polje_kolicina=Entry(master,textvariable=self.kolicina)
        polje_kolicina.grid(row=1,column=2)

        self.cena=IntVar(master,value=None)
        polje_cena=Entry(master,textvariable=self.cena)
        polje_cena.grid(row=1,column=4)

        #d
        self.poraba=IntVar(master,value=None)
        polje_poraba=Entry(master,textvariable=self.poraba)
        polje_poraba.grid(row=4,column=2)
        
        datoteka_nakup=Label(text="Račun shrani v:")
        datoteka_nakup.grid(row=2,column=0)
        self.izhodna_datoteka=StringVar(master,value=None)
        polje_izhodna_datoteka=Entry(master,textvariable=self.izhodna_datoteka)
        polje_izhodna_datoteka.grid(row=2,column=2)

        

        datoteka_nakup_b=Button(text="NAKUP",command=self.nakup)
        self.vhodna_datoteka=StringVar(master,value=None)
        datoteka_nakup_b.grid(row=2, column=4)

        gumb_izhod=Button(text="Izhod", command=master.destroy, bg="yellow")
        gumb_izhod.grid(row=4, column=4)

        gumb_konec_nakupa=Button(text="Zaključek nakupa",command=self.cenaskupaj, bg="green")
        gumb_konec_nakupa.grid(row=3,column=2)
        
        self.stevec=0
        root.title("e-Košarica")#naslov


    def nakup(self):
        self.stevec+=self.kolicina.get()*self.cena.get()
        with open(str(self.izhodna_datoteka.get())+".txt","a") as f:
            print("Naziv artikla:{}; Cena:{} EUR; Kolicina: {}x".format(self.izdelek.get().strip(),self.cena.get(),self.kolicina.get()),file=f)

    def cenaskupaj(self):
        with open(str(self.izhodna_datoteka.get())+".txt","a") as f:
            print("Znesek celotnega nakupa: {} evrov".format(self.stevec),file=f)

            print("Poraba je lahko:{}".format(self.poraba.get()),file=f)
            #ta del mi noče delat.. zakaj???
            if self.stevec<=self.poraba:
                print("Nakup je mogoč",file=f)
            else:
                print("Nakup ni mogoč",file=f)

    
                                
root=Tk()
app=KOSARICA(root)
root.mainloop()
        
