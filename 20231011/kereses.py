# Keresés: Mondjuk meg, hogy egy elembe vane a lsitában és ha igen akkor hányadik? 

from random import randint

szamok = []
for i in range(100):
    szamok.append(randint(-100,100))
print(szamok)

keresett = int(input('Keresett: szám: '))
#Megoldás v1
for i in range(len(szamok)):
    if szamok [i] == keresett: 
        print(f'A kersett szám a {i + 1}. a listában')
        break 
else: 
    print('A keresett szán nincs benne')

# megoldás v2
# univerzális 
index = 0
while index < len(szamok) and (szamok) [index] != keresett:
    index += 1
if index == len(szamok):
    print('A keresett szám nincsen benne')
else:
    print(f'A keresett szám a {index + 1}. a lsitában')

# Az első megtalált elem indexét adja vissza, hiszen utána egyből kilép a ciklusból

