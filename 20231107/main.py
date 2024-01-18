from forras import *


print(f'A versenyen {versenyzokSzama()} versenyző indult')
print(f'{legalabbDarab(8600)} olyan versenyző volt, aki legalább 8600 pontot ért el' )
print(f'A versenyzők által elért pontszámok átlaga: {atlag_pontszam():.ef)}')
gyoztes = gyoztes_index()
print(f'A veresenyző győztese {nevek(gyoztes)} {idok(gyoztes)} pontos eredménnyel')
versenyzo = int(input('Kérem adjon meg egy nevet:'))
print('A versenyző neve: {}')
print('A versenyző pontszáma: {}')

