vysvedceni = {
"cesky_jazyk": 1,
"matematika": 3,
"dejepis": 1  
}
print(vysvedceni)


sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
sales["Noc, která mě zabila"] = 0
sales["Vrah zavolá v deset"] = 5681 + 100
print(sales)

tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}
cislo_listku = int(input("Zadej cislo listku: "))
if cislo_listku in tombola:
    print(f'Cislo listku {cislo_listku} vyhrava {tombola[cislo_listku]}')
    tombola.pop(cislo_listku)
else:
        print("Bohužel nevyhráváš nic.")
        

passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}
jmeno = input("Zadej jmeno: ")