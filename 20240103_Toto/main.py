from fordulok import *

beolvas('toto.txt')

print('3. feladat: Toto')
print('3.2 feladat: Adatok beolvasása és tárolása')
print(f'3.2 feladat: Fogadási fordulok száma: {len(fordulok)}')
print(f'3.3 feladat: telitalatos szelvenyek száma: {teli_szelvenyek_szama()}darab.')
if volt_dontetlen_fordulo():
    print('3.4 feladat. Volt döntetlen forduló' )
else:
    print('3.4 feladat: Nem volt döntetlen mentes forduló')