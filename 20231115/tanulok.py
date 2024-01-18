from tanulo import tanulo
from random import choice, randint
from datetime import datetime

tanulok: list[tanulo] = []
vezeteknevek = ['Kiss', 'Kovács', 'Szabó', 'Horváth', 'Fazekas', 'Török', 'Magyar']
keresztnevek = ['Márk', 'Bálint', 'Eszter', 'Judit', 'Elemér', 'Péter', 'Pál', 'Miksa', 'Töhötöm']

def uj_tanulo() -> tanulo:
    vezeteknev = choice(vezeteknevek)
    keresztnev = choice(keresztnevek)
    szuletesi_ev = randint(2003, 2010)
    szuletesi_honap = randint(1, 12)
    szuletesi_nap = randint(1, 28)
    szuletesi_datum = datetime(szuletesi_ev, szuletesi_honap, szuletesi_nap)
    jegyek = []
    for i in range(randint(0, 5)):
        jegyek.append(randint(1, 5))
    return tanulo(vezeteknev, keresztnev, szuletesi_datum, jegyek)

def tanulok_feltolt(letszam: int) -> None:
    for i in range(letszam):
        tanulok.append(uj_tanulo())

def tanulok_kiir() -> None:
    for item in tanulok:
        print(f'{item.vezeteknev} {item.keresztnev} ({item.szuletes})')
        print(f'\tJegyei: {item.jegyek}')
        print(f'\tÁtlaga: {item.atlag()}')

def osztaly_legjobbja() -> tanulo:
    legjobb = tanulo[0]
    for item in tanulok[1:]:
        if item.atlag() > legjobb.atlag():
            legjobb = item
    return legjobb

def osszatlag() -> float:
    osszeg = 0
    for item in tanulok:
        ossszeg += item.atlag()
    return osszeg / len(tanulok)

def atlag_folott_letszam() -> int:
    """"
        Megszamolja hogy hany tanulo van az atlag folott
    """
    darab = 0
    for item in tanulok:
        if item.atlag() > osszatlag():
            darab += 1
    return darab