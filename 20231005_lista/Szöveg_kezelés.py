mondat = 'Lorem ipsum dolor sit amet'

# Szöveg = karakterek listája

# Milyen hosszú a mondat?
print(f'A mondat {len(mondat)} akárhány karakterből áll.')

# Hány szóból áll a mondat? -> megszámoljuk a szóközöket
darab = 0
# for i in range(len(mondat)):
for karakter in mondat:
    if karakter == ' ' :
        darab += 1'
print(f'A mondat {darab + 1} darab szóból áll.')


print(f'A mondatban {darab} legalább 10 karakter hosszú szó van.')

#Hány olyan szó van a mondatban, amelyik legalább 10 karakter hosszú?
#megoldás v2
darab = 0
szo_hossza = 0

for karakter in rovid_mondat:
    if karakter != ' ':
        szo_hossza += 1
    else:
        if szo_hossza >= 10
        darab += 1
        szo_hossza = 0
if szo_hossza >= 10: # az utlsó szót is meg kell vizsgálni
            darab += 1
print(f'A mondatban {darab} legalább 10 karakter hosszú szó van.')

# Hány olyan szó van a mondatban, amelyik legalább 10 karakter hosszú?
# megoldás v2
szavak = rovid_mondat.split()
darab = 0
for szo in szavak:
    if len(szo) > 0:
        darab += 1
print(f'A mondatban {darab} darab legalább 10 karakter hosszú szó van.')


# Kérjünk be egy karaktert. És mondjuk meg hogy hány darab van belőle a mondatban.

input_karakter = input('Adjon meg egy karakter: ')
for karakter in mondat:
    if karakter.lower() == input_karakter.lower(): #.lower () kisbetűvé konvertálja a stringet
        darab +=
print(f'{input_karakter} karakterek száma a mondatban: {darab}')



# meylik karakterből mennyi van?
# Melyikből van a legtöbb?

karakterek = 'kqwqqqrwrzgrettjdsddfkjsdoklsrkkj'
karakterek_szama = []

for lehetseges_karakterek in lehetseges_karakterek:
    darab = 0
    for karakter in mondat:
        if karakter.lower() == lehetseges_karakterek:
            darab += 1
    karakterek_szama.append(darab)
#print(karakterek_szama)

print('Karakter statisztika')
for i in range(len(lehetseges_karakterek)):
    print(f'{lehteseges_karakterek[i]}: {karakterek_szama[i]}')


legtobb_indexe = 0
for i in range(len(karakterek_szama)):
    if karakterek_szama[i] > karakterek_szama [legtobb_indexe]:
        legtobb_indexe = i
print(f'{lehetseges_karakterek[legtobb_indexe]} karakterből van a legtöbb {karakterek_szama[legtobb_indexe]} darab')




