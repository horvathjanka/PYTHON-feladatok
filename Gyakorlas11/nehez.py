from allat import Allat

allatok: list[Allat] = []

def legnehezebb() -> Allat:
    legnehezebb_allat = allatok[0]
    for a in allatok:
        if a.tomeg > legnehezebb_allat.tomeg:
            legnehezebb_allat = a
    return legnehezebb_allat



for i in range(3):
    nev = input('Add meg egy állatfaj nevét! ')
    tomeg = float('Hány kilogramm a tömege egy példánynak? ')
    allatok.append(Allat(nev, tomeg))

file = open('legnehezesebb.txt', 'w', encoding='utf-8')
file.write(legnehezebb().nev)
file.close

for a in allatok:
    print(f'A(z) {a.nev} tömege {a.tomeg} kilogramm')
