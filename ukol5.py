teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]
prumerna_teplota = [sum(teplota)/len(teplota) for teplota in teploty]
print([round(teplota,2) for teplota in prumerna_teplota])

ranni_teploty = [teplota[0] for teplota in teploty]
print(ranni_teploty)

nocni_teploty = [teplota_2[3] for teplota_2 in teploty]
print(nocni_teploty)

poledne = [teplota[1] for teplota in teploty]
print(poledne)

poledne_noc = {(teplota,teplota_2) for (teplota, teplota_2) in zip(poledne, nocni_teploty)}
print(poledne_noc)


#Bonus
teploty = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]
prumerna_teplota = [sum(teplota[1:5])/len(teplota[1:5]) for teplota in teploty]
prumerna_teplota = [round(teplota,2) for teplota in prumerna_teplota]
print(prumerna_teplota)
tydenni_prehled ={den[0]: teplota for (den, teplota) in zip(teploty, prumerna_teplota)}
print(tydenni_prehled)

