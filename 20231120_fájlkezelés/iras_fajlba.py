zoldseg = input('Adja meg a zöldség nevét: ')

# fajl = open('zoldsegek.txt', 'w', encoding='UTF8') 
# Írásra nyitva meg a fájlt, ha nem létezik akkor létehozza.
# a = append - hozzáfűzés


fajl = open('zoldsegek.txt', 'a', encoding='UTF8') 
# Ha létezik akkor felül írja.
# ha létezik akkor a végéhez fogja hozzáfűzni
fajl.write(zoldseg + '\n')



zoldsegek = ['Hagyma', 'burgonya', 'paradicsom', 'zeller']
for z in zoldsegek:
    fajl.write(z +'\n')


fajl.close()