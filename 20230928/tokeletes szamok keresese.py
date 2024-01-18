#Tökéletes számok

#Egy pozitív egész számot tökéletesnek nevezünk, ha a szám megegyezik az
#önmagánál kisebb osztóinak összegével. Pl. a 6 tökéletes szám, mert az
#önmagánál kisebb osztói az 1, 2, 3, és ezek összege pont 6.
#Az előző feladat mintájára, írj programot, mely bekér egy pozitív egész
#számot, majd megállapítja, hogy az tökéletes szám-e vagy nem! 

#A program várt működése pl. a következő:
#Írj be egy pozitív egész számot: 6
#Tökéletes szám!
#Írj be egy pozitív egész számot: 12
#Nem tökéletes szám.

felso_hatar = int(input('Tökéletes szám keresésének felső határa: '))

for szam in range(1, felso_hatar + 1):

print(f'Tökéletes számok 1 és {felso_hatar} között: ', end='')
for i in range(1, felso_hatar):
    osszeg = 0
    if szam % i == 0:
        osszeg += i
 
if osszeg == szam:
    print(szam, end='')