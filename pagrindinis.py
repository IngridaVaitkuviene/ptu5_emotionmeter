from tkinter import *
import matplotlib.pyplot as plt     

langas = Tk()
langas.title("Jausmomatis")
langas.geometry("380x500")

busenos_mygtukai = IntVar()

class Pagrindinis:
    def __init__(self, master):
        self.master = master
        self.tarpas = Label(self.master, text="")
        self.tarpas.grid(row=0, column=1)
        self.pavadinimas = Label(self.master, text="CodeAcademy PTU-5 Jausmomatis", width=50 )
        self.pavadinimas.grid(row=1, column=1)
        self.tarpas = Label(self.master, text="")
        self.tarpas.grid(row=2, column=1)
        self.paaiskinimas = Label(self.master, text="Pasirinkite kaip šiandien jaučiatės\n išklausius naują temą bei atlikus užduotis", width=50)
        self.paaiskinimas.grid(row=3, column=1)
        self.b_liudnas = Radiobutton(self.master, text="Liūdnas", variable=busenos_mygtukai, value=1, width=50)
        self.b_liudnas.grid(row=4, column=1)
        self.liudnas_apibudinimas = Label(self.master, text="visiškai nieko nesuprantu apie ką kalbama,\n perskaičius užduotį neaišku ko manęs prašoma atlikti", width=50)
        self.liudnas_apibudinimas.grid(row=5, column=1)    
        self.b_neutralus = Radiobutton(self.master, text="Neutralus", variable=busenos_mygtukai, value=2, width=50)
        self.b_neutralus.grid(row=6, column=1)
        self.neutralus_apibudinimas = Label(self.master, text="temą kaip ir suprantu, tačiau \nnepavyksta pilnai/greitai atlikti užduočių", width=50)
        self.neutralus_apibudinimas.grid(row=7, column=1)
        self.b_linksmas = Radiobutton(self.master, text="Linksmas", variable=busenos_mygtukai, value=3, width=50)
        self.b_linksmas.grid(row=8, column=1)
        self.linksmas_apibudinimas = Label(self.master, text="viskas aišku ir suprantama!", width=50)
        self.linksmas_apibudinimas.grid(row=9, column=1)
        self.issaugoti = Button(self.master, text='Išsaugoti pasirinkimą', command=self.issaugoti_pasirinkta, width=50)
        self.issaugoti.grid(row=10, column=1)
        self.tarpas = Label(self.master, text="")
        self.tarpas.grid(row=11, column=1)
        self.b_rezultatas = Button(self.master, text="Rezultatas", command=self.gauti_rezultata, width=50)
        self.b_rezultatas.grid(row=12, column=1)

    def issaugoti_pasirinkta(self):
        ivesta = str(busenos_mygtukai.get())
        if ivesta == "1":
            self.issaugoti["text"] = "Išsaugota Liūdnas"
        elif ivesta == "2":
            self.issaugoti["text"] = "Išsaugota Neutralus"
        elif ivesta == "3": 
            self.issaugoti["text"] = "Išsaugota Linksmas"
        self.b_liudnas.destroy()
        self.b_neutralus.destroy()
        self.b_linksmas.destroy()
        self.liudnas_apibudinimas["text"] = ''
        self.neutralus_apibudinimas["text"] = ''
        self.linksmas_apibudinimas["text"] = ''
        self.paaiskinimas["text"] = "Ačiū"
        try:
            with open("emotionmeter.txt", "a") as tekstinis_irasyti:
                tekstinis_irasyti.writelines(ivesta + "\n")
        except Exception as e:
            print(f"Nepavyko įrašyti failo {e.__class__.__name__}: {e}") 

    def gauti_rezultata(self):
        try:
            with open("emotionmeter.txt", "r") as tekstinis_gauti:
                tekstinis = tekstinis_gauti.readlines()
        except Exception as e:
            print(f"Nepavyko perskaityti failo {e.__class__.__name__}: {e}") 
        liudnas = 0
        neutralus = 0
        linksmas = 0
        for irasas in tekstinis:
            if irasas == "1\n":
                liudnas += 1
            elif irasas == "2\n":
                neutralus += 1
            elif irasas == "3\n":
                linksmas += 1
        busenos = ["Liūdnas", "Neutralus", "Linksmas"]
        suma = [liudnas, neutralus, linksmas]
        plt.bar(busenos, suma)
        plt.title("Kaip šiandien jaučiamės?")
        plt.xlabel("Būsenos")
        plt.ylabel("Suma")
        plt.show()

# class Vidinis:
#     def __init__(self, master):
#         self.master = master

programa = Pagrindinis(langas)
langas.mainloop()
