# mennyi egy megadott feltételnek megfeleő számok összege, átlaga..?

from random import randint

szamok = [randint(1,100) for i in range(100)]

for i in range(20):
    szamok.append(randint(-100,100))

print(szamok)

# mennyi a pozítiv számok összege
osszeg = 0
for szam in szamok:
    if szam > 0:
        osszeg += 0
print(f'A pozitív szamok összege: {osszeg}.')


# mennyi a páros számok átlag?
osszeg = 0
darab = 0
for szam in szamok:
    if szam % 2 == 0:
        osszeg += szam
        darab += 1 
print(f'A pozitív szamok összege: {osszeg/darab}.')
