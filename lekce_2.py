pekarna ={
    "houska": 10,
    "kolac": 15,
    "chleba": 40,
    "muffin": 20,
    "loupak": 20,
    "frgal": 50
}


produkt = input("Zadej produkt:")

if produkt in pekarna:
print(f'{produkt} stoji {pekarna["produkt"]} korun.')
else:
    print(f'Bohuzel, produkt{produkt} neprodavame.')
