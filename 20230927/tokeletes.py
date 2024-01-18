# Tökéletes számok

# Egy pozitív egész számot tökéletesnek nevezünk, ha a szám megegyezik az
# önmagánál kisebb osztóinak összegével. Pl. a 6 tökéletes szám, mert az
# önmagánál kisebb osztói az 1, 2, 3, és ezek összege pont 6.
# Az előző feladat mintájára, írj programot, mely bekér egy pozitív egész
# számot, majd megállapítja, hogy az tökéletes szám-e vagy nem! 

# A program várt működése pl. a következő:
# Írj be egy pozitív egész számot: 6
# Tökéletes szám!
# Írj be egy pozitív egész számot: 12
# Nem tökéletes szám.


szam = int(input('Írj be egy pozitív egész számot:  '))
osszeg = 0
for i in range(1, int(szam / 2) + 1):
    if szam % 1 == 0:
        osszeg = 1
if osszeg == szam:
    print('Tökéletes szám!')
else:
    print('Nem tökéletes szám.')