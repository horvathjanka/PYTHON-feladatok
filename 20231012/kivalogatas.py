# A hárommal osztható számokat pakoljuk át egy másik listába!

from random import randint

szamok = []
harommal_oszthato_szamok = []

for i in range(20):
    szamok.append(randint(-100, 100))
print(szamok)

#kiválogatás
harommal_oszthato_szamok = []
for szam in szamok:
    if szam % 3 == 0:
        harommal_oszthato_szamok.appemd(szam)
print(harommal_oszthato_szamok)

