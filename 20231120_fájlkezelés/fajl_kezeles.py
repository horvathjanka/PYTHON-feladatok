fajl = open('gyumolcsok.txt', 'r', encoding='UTF8')

egysor = fajl.readline() # brolvas egy sort a fájból és a fájl mutatót a követekező sorra állítja
egysor = egysor.strip() # levágjuk a végéről az Entert
print(egysor)

kovetekezosor = fajl.readline().strip()
print(kovetekezosor)

fajl.close()

print('-------------------------------')

# Összes beolvasása
gyumolcsok = []
fajl = open('gyumolcsok.txt', 'r', encoding='UTF8')

for sor in fajl:
    gyumolcsok.append(sor.strip())

fajl.close()

print(gyumolcsok)

# A kettő módzser kombinálása
gyumolcsok.clear()
fajl = open('gyumolcsok_fejlec.txt', 'r', encoding='UTF8')

# elso_sor = fajl.readline()
fajl.readline() # beolvassuk a, de nem tároljuk mert nincs rá szükségünk
for sor in fajl:
    gyumolcsok.append(sor.strip())

fajl.close()

print(gyumolcsok)

