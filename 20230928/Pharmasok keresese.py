#Pitagorszi hármasok keresése

#Írj programot, mely egy megadott felső határig az összes pozitív egész
#számot behelyettesíti a és b helyére, kiszámolja a hozzájuk tartozó
#megfelelő c értéket, leellenőrzi, hogy a, b, és c kielégítik-e Pitagorasz
#tételét, és ha igen, kiírja őket a képernyőre! 

#A program várt működése pl. a következő:
#Befogó max hossza: 10
#3 4 5; 4 3 5; 6 8 10; 8 6 10

from math import sqrt

limit = int(input('Befogó max hossza:  '))
print('Pitagorászi számhármasok: ')
for a in range(1,limit):
    for b in range (a, limit):
        c = sqrt (a**2 + b**2)
        if round(c) == c:
            print(f'({a},{b},{int(c)})')



