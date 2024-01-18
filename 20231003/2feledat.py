#2. feladat

# Kérje be 3 felhasználó nevét és életkorát.
# Az életkort addig kérje, amíg nem megfelelő értéket kap. (18-99)
# Határozza meg, hogy ki a legidősebb!

legidosebb_neve = ''
legidosebb_elekora = -1

for i in range(3):
    nev = input("Név: ")
    eletkor = -1
    while eletkor<18 or eletkor>100:
        eletkor = int(input('Életkor: '))
    if eletkor > legidosebb_elekora:
        legidosebb_neve = nev
        legidosebb_elekora = eletkor
print(f'Legidősebb: {legidosebb_neve}, életkora: {legidosebb_elekora}')