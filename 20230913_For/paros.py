# Írjuk ki a páros számokat megadott 2 végérték között!

eleje = int(input('Eleje: '))
vege = int(input('Vége: '))

if eleje % 2 != 0:
    eleje += 1
for i in range(eleje, vege, 2):
    print(i, end=' ')