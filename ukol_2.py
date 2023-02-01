sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
nakup = input("Zadejte nazev produktu: ")
mnozstvi = input("Zadejte pocet: ")
#klic ="1N4148"
#print(f'{nakup} je na skladě {sklad[klic]}')
#if nakup in sklad:
    #sklad[nakup] = int(sklad[nakup]) -int(mnozstvi)
    #print(f'{nakup} na skladě zbývá {sklad[nakup]} ks.')
#else:
    #print(f'{nakup} není skladem dostupné.')
#if int(mnozstvi) >= int(sklad[nakup]):
  #print(f'{nakup} na skladě máme jen {sklad[nakup]} ks.')
  #sklad.pop(nakup)
  #print(sklad)
if int(mnozstvi) < int(sklad[nakup]):
  print(f'Můžeme Vám dodat dostatečné množství součástek.')
sklad[nakup] = sklad[nakup] - int(mnozstvi)
print(f'Produkt{nakup} zůstalo na skladě {sklad[nakup]} ks')
print(sklad)