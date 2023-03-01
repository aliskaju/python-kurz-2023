#1.\d?\d[.|/] ?\d[.|/] ?\d{4}
#2.\d{3} \d{2} +[A-Z] ?\w* ?\w* ?\w* ?
#bonus
import re
#uzivatelke_jmeno
overeni_1 =re.compile(r"[a-zA-Z]{6,10}")
uzivatelske_jmeno = input("zadejte uzivateske jmeno: ")
vstup_1 = overeni_1.fullmatch(uzivatelske_jmeno)
if vstup_1 == None:
    print("Neplatné uživatelské jméno!")
else:
#heslo
    overeni_2 =re.compile(r"[\w=_+.-]{12,30}")
    heslo = input("zadejte heslo: ")
    vstup_2 = overeni_2.fullmatch(heslo)
    if vstup_2 == None:
        print("Neplatné heslo!")
    else:
#validni_email
        overeni_3 =re.compile(r"\"?\w+.?\-?\w+?\"?@\[?\w+?\-?\w+?\.(\w+\.?){1,3}\]?")
        email = input("zadejte email: ")
        vstup_3 = overeni_3.fullmatch(email)
        if vstup_3 == None:
            print("Neplatný email!")
        else:
            print("Hurá, přihlášení proběhlo v pořádku!")