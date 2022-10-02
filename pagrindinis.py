from tkinter import *
import matplotlib.pyplot as plt
from tkinter.ttk import *
from PIL import ImageTk, Image 

langas = Tk()
langas.title("Jausmomatis")
langas.geometry("350x580")
ikonele = PhotoImage(file="happy1.png")
langas.iconphoto(True, ikonele)
busenos_mygtukai = IntVar()
sad_btn = PhotoImage(file="sad-face1.png")
neutral_btn = PhotoImage(file="neutral-face1.png")
smile_btn = PhotoImage(file="happy1.png")
sriftas = "Comic Sans MS", 10, "normal"
sriftas1 = "Comic Sans MS", 15, "normal"

class Pagrindinis:
    def __init__(self, master):
        self.master = master
        self.pavadinimas = Label(self.master, text="Asmeninis jausmomatis", justify=CENTER, font=sriftas1)
        self.pavadinimas.grid(row=1, column=1, padx=10, pady=10)
        self.paaiskinimas = Label(self.master, text="Pasirinki kaip šiandien jautiesi\n išklausius naują temą bei atlikus užduotis", justify=CENTER, font=sriftas)
        self.paaiskinimas.grid(row=3, column=1, padx=10, pady=10)
        self.b_liudnas = Radiobutton(self.master, image=sad_btn, variable=busenos_mygtukai, value=1)
        self.b_liudnas.grid(row=4, column=1)
        self.liudnas_apibudinimas = Label(self.master, text="visiškai nieko nesuprantu apie ką kalbama,\n perskaičius užduotį neaišku ko manęs prašoma atlikti", justify=CENTER, font=sriftas)
        self.liudnas_apibudinimas.grid(row=5, column=1)    
        self.b_neutralus = Radiobutton(self.master, image=neutral_btn, variable=busenos_mygtukai, value=2)
        self.b_neutralus.grid(row=6, column=1)
        self.neutralus_apibudinimas = Label(self.master, text="temą kaip ir suprantu, tačiau \nnepavyksta pilnai/greitai atlikti užduočių", justify=CENTER, font=sriftas)
        self.neutralus_apibudinimas.grid(row=7, column=1)
        self.b_linksmas = Radiobutton(self.master, image=smile_btn, variable=busenos_mygtukai, value=3)
        self.b_linksmas.grid(row=8, column=1)
        self.linksmas_apibudinimas = Label(self.master, text="viskas aišku ir suprantama!", justify=CENTER, font=sriftas)
        self.linksmas_apibudinimas.grid(row=9, column=1)
        self.issaugoti = Button(self.master, text='Išsaugoti pasirinkimą', command=self.issaugoti_pasirinkta, width=35)
        self.issaugoti.grid(row=10, column=1, padx=10, pady=10)
        self.b_rezultatas = Button(self.master, text="Rezultatas", command=self.gauti_rezultata, width=35)
        self.b_rezultatas.grid(row=12, column=1, padx=10, pady=10)
        self.b_naujas = Button(self.master, text="Gyvenimo moto. Spausk čia!", command=self.naujas_langas, width=35)
        self.b_naujas.grid(row=14, column=1, padx=10, pady=10)
        self.b_uzdaryti = Button(self.master, text="Uždaryti programą", command=self.uzdaryti_langa, width=35)
        self.b_uzdaryti.grid(row=16, column=1, padx=10, pady=10)

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
        self.paaiskinimas["text"] = "Puiku, tavo rezultatas išsaugotas!"
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
        spalvos = ["gray", "silver", "gainsboro"]
        plt.bar(busenos, suma, color=spalvos)
        plt.title("Rezultatas")
        plt.xlabel("Būsenos")
        plt.ylabel("Suma")
        plt.show()

    def uzdaryti_langa(self):
        self.master.destroy()

    def naujas_langas(self):
        self.vidinis = Toplevel(self.master)
        self.naujas = Vidinis(self.vidinis)
   
class Vidinis:
    def __init__(self, master):
        self.master = master
        self.paveikslelis = ImageTk.PhotoImage(Image.open("image/if_sad1.JPG"))
        self.image = Label(self.master, image=self.paveikslelis)
        self.image.pack(side=BOTTOM, fill=BOTH, expand=YES)

programa = Pagrindinis(langas)
langas.mainloop()
