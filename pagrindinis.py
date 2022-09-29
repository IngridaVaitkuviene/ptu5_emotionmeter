# padaryti programą, kur studentai galėtų kasdien pasižymėti savo jauseną dienos temos/uždavinių atžvilgiu. 
# pvz liūdnas veidelis - nesuprantu, neišeina išspręsti uždavinių, linksmas - viskas aišku, uždaviniai suprantami ir pan. 
# ir programa apibendrintų visas įvestis ir grąžintų rezultatą apie studentų savijautą

from tkinter import *

langas = Tk()
langas.title("Jausmomatis")
langas.geometry("500x600")

busenos = IntVar

class Pagrindinis:
    def __init__(self, master):
        self.master = master
        self.pavadinimas = Label(self.master, text="CodeAcademy PTU-5 Jausmomatis")
        self.pavadinimas.pack()
        self.paaiskinimas = Label(self.master, text="Pasirinkite kaip šiandien jaučiatės išklausius naują temą bei atlikus užduotis")
        self.paaiskinimas.pack()
        self.b_liudnas = Radiobutton(self.master, text="Liūdnas", command=self.pasirinktas())
        self.b_liudnas.pack()
        self.liudnas_apibudinimas = Label(self.master, text="visiškai nieko nesuprantu apie ką kalbama,\n perskaičius užduotį neaišku ko manęs prašoma atlikti")
        self.liudnas_apibudinimas.pack()      
        self.b_neutralus = Radiobutton(self.master, text="Neutralus", command=self.pasirinktas())
        self.b_neutralus.pack()
        self.neutralus_apibudinimas = Label(self.master, text="temą kaip ir suprantu, tačiau nepavyksta pilnai/greitai atlikti užduočių")
        self.neutralus_apibudinimas.pack()
        self.b_linksmas = Radiobutton(self.master, text="Linksmas", command=self.pasirinktas())
        self.b_linksmas.pack()
        self.linksmas_apibudinimas = Label(self.master, text="viskas aišku ir suprantama!")
        self.linksmas_apibudinimas.pack()
        self.b_rezultatas = Button(self.master, text="Rezultatas", command=self.gauti_rezultata())
        self.b_rezultatas.pack()

    def pasirinktas(self):
        pass

    def gauti_rezultata(self):
        self.vidinis = Toplevel(self.master)
        self.naujas = Vidinis(self.vidinis)

class Vidinis:
    def __init__(self, master):
        self.master = master

programa = Pagrindinis(langas)
langas.mainloop()