szo1 = input('Adje meg egy szót: ')
szo2 = input('Adje meg egy másik szót: ')
if len(szo1) > len(szo2):
    print(f'{szo1} hosszabb, mint {szo2}')
elif len(szo1) < len(szo2):
    print(f'{szo1} rövidebb, mint {szo2}')
else:
    print(f'{szo1} és {szo2} hossza egyenlő')