# string kezelhető listaként
s: str = "Lorem ipsum dolor sit amet."
print(f'A szöveg hossza: {len(s)}')
print(f'A szöveg 3. karaktere: {s[2]}') # 0, 1, 2
#for betu in s:
#    print(betu)

# Soroljuk fel hogy milyen betűk vannak a szövegben (minden betű csak egyswzer szerepeljen.)
betuk = ""
for betu in s:
    if betu not in betuk:
        betuk += betu
print(betuk)

print(f'Nagybetűs szöveg: {s.upper()}')
print(f'Kisbetűs szöveg {s.lower()}')
print(f'Első nagy betű {s.capitalize()}') # az első betű nagybetű



gyumolcsok = ['alma', 'körte' ,'narancs', 'paradicsom']
for gyumolcs in gyumolcsok:
    #15 karakter hosszan jobbra ígazitva kitöltve a helyet
    print(gyumolcs.rjust(15, "-"))



szavak = s.split(' ')
print(szavak)



s2 = " 12;34;334;56;67;21"
# mennyi az s2-ben lévő ;-vel tagolt számok összege?
szamok = s.split(';')
osszeg = 0
for szam in szamok:
    osszeg += int(szam)
print(osszeg)



s3 = "mdeffojfedfre"
if s3.isalpha() == True:
    print('A szövegben csak az abc betűi vannak.')
else:
    print('A szövegben NEM csak az abc betűi vannak')


if s3.isalnum() == True:
    print('A szövegben csak az abc betűi és számok vannak.')
else:
    print('A szövegben NEM csak az abc betűi és számok vannak')



s4 = "dassh ad ad "
# white space: szóköz, enter, tab
print(s4)
if s4.strip() == "szöveg":
    print('s4 = szöveg')
else:
    print('s4 != szöveg')

