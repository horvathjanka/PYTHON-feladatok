from dolgozat_megoldas import *

koridok = ['01:17:565', '01:16:258', '01:15:711', '01:16:437', '01:16:764', '01:16:964', '01:15:185', '01:15:573', '01:15:078', '01:15:723', '01:17:284', '01:15:929', '01:15:382', '01:17:378', '01:17:961', '01:15:348', '01:17:303', '01:16:233', '01:17:665', '01:15:050' ]
koridok_mp = koridokMasodpercben(koridok)

print(f'{versenyzokSzama{koridok}} versenyző indult a futamon.')
# print(f'{len{koridok}} versenyző indult a futamon.')

print('A leggyorsabb versenyző:')
print(f'\tRajtszáma: {leggyorsabb_rajtszama(koridok_mp)}')
print(f'\tKörideje: {koridok[leggyorsabb_rajtszama(koridok_mp)]}')
print(f'Az átlagos köridő: {atlagos_koridok(koridok_mp):.3f}')
print(f'{lassabb_mint_atlag (koridok_mp)} versenyző lasssabb volt az átlag.')
rajtszam = int(input('Kérek egy rajtszámot: '))
print(f'A {rajtszam} rajtszámú versenyző körideje: {koridok[rajtszam]}')
print(f'A {rajtszam} rajtszámú versenyző körideje másodpercben: {koridok_mp[rajtszam]}')
rajtszam2 = int(input('Kérek még egy rajtszámot:'))
kulonbseg = abs(koridok_mp[rajtszam] - koridok_mp[rajtszam2])
#if kulonbseg < 0:
    #kulonbseg*= -1

print(f'A {rajtszam} és a {rajtszam2} számú versenyzők közöti különbség: {kulonbseg:.3f}')