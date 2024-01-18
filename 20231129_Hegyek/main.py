from HegyekMo import *

beolvas('hegyekMO.txt')
print(f'3. feladat: Hegycsúcsok száma: {hegyek_szama()} db')
print(f'4. feladat: Hegycsúcsok átlagos magassága: {atlag_magassag()} m.')
print(f'5. feladat: A legmagasabb hegycsúcs adatai:')
legmagasabb = legmagasabb_hegy()
print(f'\tNév: {legmagasabb.nev}')
print(f'\tHegység: {legmagasabb.hegyseg}')
print(f'\tMagasság: {legmagasabb.magassag}')
magassag = int(input('6. feladat: Kérek egy magasságot: '))
if van_magasabb(magassag):
    print(f'\tVan {magassag} m-nél magasabb hegycsúcs.')
else:
    print(f'\tNincs {magassag} m-nél magasabb hegycsúcs.')
print(f'7. feladat: 3000 lábnál magasabb hegycsúcsok száma: {darab_magasabb_mint(3000)} db.')

print('8. feladat: Hegység statisztika:')
for key, value in hegy_statisztika().items():
    print(f'\t{key}: {value} db')

mentes('Bükk-vidék', 'bukk-videk.txt')