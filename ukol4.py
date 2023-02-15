def format_cisla(tel_cislo):
    znaky = len(tel_cislo)
    if znaky == 13 and tel_cislo [0:4] == "+420":
        overeni = True
    elif znaky == 9:
        overeni = True
    else:
        overeni = False
    return overeni
tel_cislo = input("Zadejte telefonni cislo: ")

if format_cisla(tel_cislo) == False:
    print(f"Bylo zadáno špatné číslo {tel_cislo}")
    exit()

def cena_za_zpravu(zprava,cena = 3, pocet_znaku = 180):
    delka = len(zprava)
    pocet_sms = delka//pocet_znaku
    if delka > 0:
        pocet_sms = pocet_sms + 1
    cena_celkem = cena * pocet_sms

    return cena_celkem 
zprava = input("Zadejte zpravu: ")
platba = cena_za_zpravu(zprava)  
print(f"Cena za zpravu je {platba} Kč.")