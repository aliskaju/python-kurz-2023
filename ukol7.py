class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km, dostupne = True):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = dostupne

    #def __str__(self):
        #return f"Auto {self.typ_vozidla} má tuhle registrační značku {self.registracni_znacka}"
    
    def pujc_auto(self):
            if self.dostupne == True:
                self.dostupne = False
                print("Potvrzuji zapůjčení vozidla")
            else:
                print("Vozidlo není k dispozici")

    def get_info(self):
        return f"Auto {self.typ_vozidla} má tuhle registrační značku {self.registracni_znacka}"
    
    def vrat_auto(self, stav_tachometru, pocet_dni):
        if self.dostupne == False:
             self.stav_tachometru = stav_tachometru
             self.pocet_dni = pocet_dni
             self.dostupne = True
        else:
            print("Vozidlo není vypůjčené")
        
    def dej_cenu(self):
        if self.pocet_dni < 7:
                cena = self.pocet_dni * 400
        else:
                cena = self.pocet_dni * 300
        return f"Cena za zapůjčené auto je {cena} Kč."     

def vyber_auto():
    auto = input("Zadejte typ auta peugeot nebo škoda: ")

    if auto == 'peugeot':
        print(peugeot.get_info())
        print(peugeot.pujc_auto())
    elif auto == 'škoda':
        print(skoda.get_info())
        print(skoda.pujc_auto())
    else:
        print('Takové auto nemáme') 
         
peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", "47534")        
skoda = Auto("1P3 4747", "Škoda Octavia", "41253")

# vyberu škoda, jde to
vyber_auto()
# vyberu škoda, nejde to
vyber_auto()
# vrátím škoda
skoda.vrat_auto(123, 10)
# cena za škoda
print(skoda.dej_cenu())
# vyberu škoda, už to zase jde
vyber_auto()






