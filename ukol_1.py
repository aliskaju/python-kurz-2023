jmeno = "Alisa"
domena = "czechitas.cz"
email_adresa = jmeno + "@" + domena
print(email_adresa)

jmeno_a_prijmeni = str(input("Zadejte prosim jmeno a prijmeni: "))
print(jmeno_a_prijmeni.upper())
print(jmeno_a_prijmeni.lower())
print(jmeno_a_prijmeni.title())

jmeno = str(input("Zadejte prosim jmeno: "))
prijmeni = str(input("Zadejte prosim prijmeni: "))
inicialy = jmeno[0] + prijmeni[0]
print(inicialy.upper())