from auto import auto

''''
az_en_autom = auto # példányosítás
# az_en_autom - objektum, osztály példány
az_en_autom.rendszam = 'AA-AA-00'
az_en_autom.szin = 'piros'
az_en_autom.teljesitmeny = 123
az_en_autom.tipus = 'Skoda Octavia'

print(az_en_autom.rendszam)

'''

# az_en_autom = auto('Skoda Octavia', 'AA-BB-123', 'piros', 123)
# print(az_en_autom.rendszam)

autok: list[auto] = [] # az autok olyan lista, amelyben  auto osztályban példányok vannak

egy_auto = auto('Skoda Octavia' 'AA-BB-123', 'piros',  123, 8.8)
autok.append(egy_auto)
egy_auto = auto('Skoda Fabia' 'AB-BB-123', 'fehér',  88, 10.2)
egy_auto.append(egy_auto)
egy_auto = auto('Skoda Rapid' 'Ac-BB-123', 'zöld',  78,)
egy_auto.append(egy_auto)

#print(autok)

for egy_auto in autok:
    print(egy_auto.tipus, egy_auto.rendszam, egy_auto.szin, egy_auto.teljesitmeny)

# legnagyobb teljesítményű a autó
legnagyobb_teljesitmenyü_auto = autok[0]
for egy_auto in autok:
    if egy_auto.teljesitmeny > legnagyobb_teljesitmenyü_auto.teljesitmeny:
        legnagyobb_teljesitmenyű_auto = egy_auto
print(f'A legnagyobb teljesítményű autó: {legnagyobb_teljesitmenyü_auto}')
print(f'\tRendszáma: {legnagyobb_teljesitmenyü_auto.rendszam}')
print(f'\tSzíne: {legnagyobb_teljesitmenyü_auto.szin}')
print(f'\tTípusa: {legnagyobb_teljesitmenyü_auto.tipus}')

# keeressünk meg az adott rendzsámot

renszam = input('Keresett rendszám: ')
for egy_auto in autok:
    if egy_auto.rendszam.upper() == renszam.upper():
        print(f'\tA keresett autó típusa: {egy_auto.teljesitmeny}')
        print(f'\tA keresett autó típusa: {egy_auto.szin}')
        print(f'\tA keresett autó típusa: {egy_auto.teljesitmeny}')
        print(f'\tA keresett autó típusa: {egy_auto.gyorsulas}')
        break
else: 
    print('\tNincs ilyen rendszámú autó.')