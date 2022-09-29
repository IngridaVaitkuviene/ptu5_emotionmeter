# padaryti programą, kur studentai galėtų kasdien pasižymėti savo jauseną dienos temos/uždavinių atžvilgiu. 
# pvz liūdnas veidelis - nesuprantu, neišeina išspręsti uždavinių, linksmas - viskas aišku, uždaviniai suprantami ir pan. 
# ir programa apibendrintų visas įvestis ir grąžintų rezultatą apie studentų savijautą

from tkinter import *

langas = Tk()
langas.title("Jausmomatis")
langas.geometry("400x500")


busenos_mygtukai = IntVar()

class Pagrindinis:
    def __init__(self, master):
        self.master = master
        self.pavadinimas = Label(self.master, text="CodeAcademy PTU-5 Jausmomatis", )
        self.pavadinimas.grid(row=0, columnspan=5)
        self.paaiskinimas = Label(self.master, text="Pasirinkite kaip šiandien jaučiatės išklausius naują temą bei atlikus užduotis")
        self.paaiskinimas.grid(row=1, column=1)
        self.b_liudnas = Radiobutton(self.master, text="Liūdnas", variable=busenos_mygtukai, value=1, command=self.pasirinktas)
        self.b_liudnas.grid(row=2, column=1)
        self.liudnas_apibudinimas = Label(self.master, text="visiškai nieko nesuprantu apie ką kalbama,\n perskaičius užduotį neaišku ko manęs prašoma atlikti")
        self.liudnas_apibudinimas.grid(row=3, column=1)    
        self.b_neutralus = Radiobutton(self.master, text="Neutralus", variable=busenos_mygtukai, value=2, command=self.pasirinktas)
        self.b_neutralus.grid(row=4, column=1)
        self.neutralus_apibudinimas = Label(self.master, text="temą kaip ir suprantu, tačiau nepavyksta pilnai/greitai atlikti užduočių")
        self.neutralus_apibudinimas.grid(row=5, column=1)
        self.b_linksmas = Radiobutton(self.master, text="Linksmas", variable=busenos_mygtukai, value=3, command=self.pasirinktas)
        self.b_linksmas.grid(row=6, column=1)
        self.linksmas_apibudinimas = Label(self.master, text="viskas aišku ir suprantama!")
        self.linksmas_apibudinimas.grid(row=7, column=1)
        self.tarpas = Label(self.master, text='')
        self.tarpas.grid(row=8, column=1)
        self.b_rezultatas = Button(self.master, text="Rezultatas", command=self.gauti_rezultata)
        self.b_rezultatas.grid(row=9, column=1)

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