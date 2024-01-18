szam1 = int(input('Adje meg egy számot: '))
szam2 = int(input('Adje meg egy másik számot: '))
if szam1 > szam2:
    print(f'{szam1} nagyobb, mint {szam2}')
elif szam1 < szam2:
    print(f'{szam1} kisebb, mint {szam2}')
else:
    print(f'{szam1} és {szam2} egyenlő')