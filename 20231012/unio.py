
# unio

from random import randint

szamok1 = []
szamok2 = []

for i in range(20):
    szamok1.append(randint(-100, 100))
    szamok2.append(randint(-100, 100))
print('szamok 1:', szamok1)
print("Szamok 2: ", szamok2)



#szétválogatás
metszet = []
for szam in szamok1:
    if szam in szamok2:
        metszet.append(szam)
print('Metszet:', metszet)
