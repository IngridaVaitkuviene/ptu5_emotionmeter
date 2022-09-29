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

programa = Pagrindinis(langas)
langas.mainloop()