from tkinter import *

langas = Tk()
langas.title("Jausmomatis")
langas.geometry("500x600")

class Pagrindinis:
    def __init__(self, master):
        self.master = master
        self.pavadinimas = Label(self.master, text="CodeAcademy PTU-5 Jausmomatis")
        self.pavadinimas.pack()
        self.paaiskinimas = Label(self.master, text="Pasirinkite kaip šiandien jaučiatės išklausius naują temą bei atlikus užduotis")
        self.paaiskinimas.pack()
        self.b_liudnas = Button(self.master, text="Liūdnas")
        self.b_neutralus = Button(self.master, text="Neutralus")
        self.b_linksmas = Button(self.master, text="Linksmas")
        self.b_liudnas.pack()
        self.b_neutralus.pack()
        self.b_linksmas.pack()
        self.b_rezultatas = Button(self.master, text="Rezultatas")
        self.b_rezultatas.pack()


programa = Pagrindinis(langas)
langas.mainloop()