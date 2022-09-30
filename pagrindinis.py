from tkinter import *
import pickle
import matplotlib.pyplot as plt

sarasas = []

def irasyti(sarasas):
    sarasas.append(busenos_mygtukai.get())
    try:
        with open("Pickle/emotionmeter.pkl", "wb") as pickle_irasyti:
            pickle.dump(sarasas, pickle_irasyti)
    except Exception as e:
        print(f"Nepavyko įrašyti failo {e.__class__.__name__}: {e}") 
        
def gauti_pasirinktus():
    try:
        with open("Pickle/emotionmeter.pkl", "rb") as pickle_gauti:
            pasirinkimai = pickle.load(pickle_gauti)
    except:
        pasirinkimai = []
    print(pasirinkimai)

langas = Tk()
langas.title("Jausmomatis")
langas.geometry("400x500")

busenos_mygtukai = IntVar()

class Pagrindinis:
    def __init__(self, master):
        self.master = master
        self.pavadinimas = Label(self.master, text="CodeAcademy PTU-5 Jausmomatis", width=50 )
        self.pavadinimas.grid(row=0, column=1)
        self.paaiskinimas = Label(self.master, text="Pasirinkite kaip šiandien jaučiatės\n išklausius naują temą bei atlikus užduotis", width=50)
        self.paaiskinimas.grid(row=1, column=1)
        self.b_liudnas = Radiobutton(self.master, text="Liūdnas", variable=busenos_mygtukai, value=1, width=50) #command=self.pasirinktas)
        self.b_liudnas.grid(row=2, column=1)
        self.liudnas_apibudinimas = Label(self.master, text="visiškai nieko nesuprantu apie ką kalbama,\n perskaičius užduotį neaišku ko manęs prašoma atlikti", width=50)
        self.liudnas_apibudinimas.grid(row=3, column=1)    
        self.b_neutralus = Radiobutton(self.master, text="Neutralus", variable=busenos_mygtukai, value=2, width=50) #command=self.pasirinktas)
        self.b_neutralus.grid(row=4, column=1)
        self.neutralus_apibudinimas = Label(self.master, text="temą kaip ir suprantu, tačiau \nnepavyksta pilnai/greitai atlikti užduočių", width=50)
        self.neutralus_apibudinimas.grid(row=5, column=1)
        self.b_linksmas = Radiobutton(self.master, text="Linksmas", variable=busenos_mygtukai, value=3, width=50) #command=self.pasirinktas)
        self.b_linksmas.grid(row=6, column=1)
        self.linksmas_apibudinimas = Label(self.master, text="viskas aišku ir suprantama!", width=50)
        self.linksmas_apibudinimas.grid(row=7, column=1)
        self.tarpas = Button(self.master, text='Išsaugoti pasirinkimą', command=self.issaugoti_pasirinkta, width=50)
        self.tarpas.grid(row=8, column=1)
        self.b_rezultatas = Button(self.master, text="Rezultatas", command=gauti_pasirinktus, width=50)
        self.b_rezultatas.grid(row=9, column=1)

    def issaugoti_pasirinkta(self):
        ivesta = busenos_mygtukai.get()
        if ivesta == 1:
            self.tarpas["text"] = "Išsaugota Liūdnas"
        elif ivesta == 2:
            self.tarpas["text"] = "Išsaugota Neutralus"
        else: 
            self.tarpas["text"] = "Išsaugota Linksmas"
        self.b_liudnas.destroy()
        self.b_neutralus.destroy()
        self.b_linksmas.destroy()
        self.liudnas_apibudinimas["text"] = ''
        self.neutralus_apibudinimas["text"] = ''
        self.linksmas_apibudinimas["text"] = ''
        self.paaiskinimas["text"] = "Ačiū"
      
    def gauti_rezultata(self):
        busenos = []
        suma = []
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
