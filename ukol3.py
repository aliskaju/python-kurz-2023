import json
with open('body.json', encoding='utf-8') as novy_soubor:
    data = json.load(novy_soubor)

print(data)

prospech = {}
for key, value in data.items():
    prospech[key] = value
    if prospech[key] >= 60:
        prospech[key] = "Pass"
    else:
        prospech[key] = "Fail"
        
print(prospech)

with open("prospech_2.json", "w", encoding="utf-8") as soubor_2:
    json.dump(prospech, soubor_2, ensure_ascii=False)