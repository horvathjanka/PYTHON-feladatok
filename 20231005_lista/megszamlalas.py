# számoljuk meg hogy hány elem felel meg egy adott feltételnek 

from random import randint

szamok = []

for i in range(randint(10,40)): 
    szamok.append(randint(1,100))

print(szamok)

# hány elem van a listában?
print(f'{len(szamok)}darab szám került generálásra.')

# hány páros szám van a listában?
paros_szam_darab = 0
for szam in szamok:
    if szam % 2 == 0:
        paros_szam_darab += 1
print(f'{paros_szam_darab} páros szán van a számok között.')

# hány negetív szám van a listában?
paros_szam_darab = 0
for szam in szamok:
    if szam % 2 == 0:
        paros_szam_darab += 1
print(f'{paros_szam_darab} páros szán van a számok között.')


