from autok import *
from os import system

autok_betolt()
while True:
    print('0 - Kilép')
    print('1 - Új auto adatainak megadása')
    print('2 - Adatok listázása')
    print('3 - Legerősebb autó')
    print('4 - Adott színű autok listázása')
    valasz = input('Választás: ')
    match valasz:
        case '0':
            break
        case '1':
            auto_beker()
        case '2':
            print('A nyiilvántartásban lévő autók:')
            autok_kiir()
            input('Tovább...')
        case '3':
            legerosebb_auto = legerosebb()
            print('A legerősebb autó adatai:')
            print(f'\tRendszám: {legerosebb_auto.rendszam}')
            print(f'\tTípus: {legerosebb_auto.tipus}')
            print(f'\tMárka: {legerosebb_auto.marka}')
            print(f'\tSzín: {legerosebb_auto.szin}')
            print(f'\tTeljesítmény: {legerosebb_auto.teljesitmeny}')
            input('Tovább...')
        case '4':
            szin = input('Milyen színű autókat listázzunk?')
            print(f'{szin}) színű autok:')
            autok_kiir(autok_szin_alapjan(szin))
            input('Tovább...')