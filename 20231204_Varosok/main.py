from varosok import *

beolvas('varosok.txt')
print(f'3. feladat: Városok száma: {varosok_szama()} db')
print(f'4. feladat: indiai nagyvárosok lakosságának összege: {orszag_lakossaga("India")} fő')
print(f'4.1 feladat: indiai nagyvárosok lakosságának összege: {orszag_lakossaga("Kína")} fő')
legnagyobb = legnagyobb_varos()
print('5. feladat: A legnagyobb város adatai: ')
print(f'\tNév: {legnagyobb.varos}')
print(f'\tOrszág: {legnagyobb.orzsag}')
print(f'\tLakosság: {legnagyobb.lakossag}')
if orszag_keres('Magyarország'):
    print('6.feladat: Van magyar város az adatok között.')
else:
    print('6.feladat: Nincs magyar város az adatok között')

print(f' 7.1 feladat: Városok egy szóközzel: {szokozos_varosok_szama(1)} db.')

print('8. feladat: Ország statisztika')
stat = orszag_statisztika()
for key, value in orszag_statisztika().items():
    print(f'\t{key} - {value} db')

orszag_mentes('kína.txt', 'Kína')