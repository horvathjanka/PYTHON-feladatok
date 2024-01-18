from eredmenyek import *


betolt('ub2017egyeni.txt')
print(f'3.2 feladat: Futók száma: {len(eredmenyek)}')
print(f'3.3 feladat: Célba érkező női sportolók: {versenyzok_szama_celban("Noi")}')
print(f'3.4 fealdat: A leghoszabb nevű futó: ')
leghoszabb_nevu_futo = leghoszabb_nevu()
print(f'\nNév: {leghoszabb_nevu_futo.Versenyz}')
print(f'\nNév: {leghoszabb_nevu_futo.Rajtszam}')
print(f'\nNév: {leghoszabb_nevu_futo.Versenyido}')
print(f'3.5 feladat: Férfi sportolók átlagos ideje: {atlag_ido("Ferfi")}óra')