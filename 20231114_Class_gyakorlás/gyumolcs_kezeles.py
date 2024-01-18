from gyumolcs import gyumolcs
from random import randint, choice

# gyumolcsok = []
gyumolcsok : list[gyumolcs] = [] # Olyan lista, amelyben gyumolcs osztálypéldányok vannak benne.
gyumolcs_nevek = ['alma', 'körte', 'meggy', 'cseresznye', 'dinnye', 'eper', 'narancs', 'banán', 'szilva']

def random_gyumolcs(min_mennyiseg: int = 1, max_mennyiseg: int = 100) -> gyumolcs:
    """
    Visszaad egy véletlenszerűen generált gyumolcs osztály példányt.
    """

    # egy_random_gyumolcs = lehetseges_gyumolcsok[randint(0, len(lehetseges_gyumolcsok)-1)]
    egy_random_gyumolcs = choice(gyumolcs_nevek)

    egy_gyumolcs = gyumolcs(egy_random_gyumolcs, randint(min_mennyiseg, max_mennyiseg), randint(300, 600))
    return egy_gyumolcs

def random_gyumolcs2(min_mennyiseg: int = 1, max_mennyiseg: int = 100) -> None:
    """
    Minden fajta gyümölcshöz genrál egy random mennyiséget és árat.
    """
    for nev in gyumolcs_nevek:
        egy_gyumolcs = gyumolcs(nev, randint(min_mennyiseg, max_mennyiseg), randint(300, 600))
        gyumolcsok.append(egy_gyumolcs)

def gyumolcsok_feltolt(mennyiseg: int) -> None:
    for i in range(mennyiseg):
        # gyumolcsok.append(random_gyumolcs())
        gyumolcsok.append(random_gyumolcs(100, 200))

def gyumolcsok_kiir() -> None:
    for egy_gyumolcs in gyumolcsok:
        print(f'{egy_gyumolcs.nev} - {egy_gyumolcs.mennyiseg}kg - {egy_gyumolcs.ar}Ft')

def teljes_keszlet_erteke() -> int:
    """
    Megszámolja és visszaadja a gyümölcsökben fekvő teljes pénzösszeget.
    """
    osszeg = 0
    for egy_gyumolcs in gyumolcsok:
        osszeg += egy_gyumolcs.mennyiseg * egy_gyumolcs.ar
    return osszeg

def legdragabb_gyumolcs() -> gyumolcs:
    legdragabb = gyumolcsok[0]
    for egy_gyumolcs in gyumolcsok:
        if egy_gyumolcs.ar > legdragabb.ar:
            legdragabb = egy_gyumolcs
    return legdragabb

def legtobb_penz_per_gyumolcs() -> gyumolcs:
    """
    Visszaadja, hogy melyik az a gyümölcs, amelyikben a legtöbb pénz áll.
    """
    legtobb = gyumolcsok[0]
    for egy_gyumolcs in gyumolcsok:
        if egy_gyumolcs.mennyiseg * egy_gyumolcs.ar > legtobb.mennyiseg * legtobb.ar:
            legtobb = egy_gyumolcs
    return legtobb