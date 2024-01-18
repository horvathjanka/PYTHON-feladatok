from gyumolcs import gyumolcs
from random import randint, choice

# gyumolcsok = []
gyumolcsok : list[gyumolcs] = [] # Olyan lista amelyben, gyumolcs osztálypéldányok vannak benne
lehetseges_gyumolcsok = ['alma', 'körte', 'meggy', 'cseresznye', 'dinnye', 'eper', 'narancs', 'banán', 'szilva' ]



def legtobb_penz_per_gyumolcs( )-> gyumolcs:
    """
    Visszadja, hogy melyik 
    """
    for egy_gyumolcs in gyumolcsok:
        if egy_gyumolcs.mennyiseg * egy_gyumolcs.ar > legtobb.meynniseg * legtobb.ar:
            legtobb = egy_gyumolcs
    return legtobb

def legdragabb_gyumolcs( )-> int:
    legdragabb = gyumolcs[0]
    for egy_gyumolcs in gyumolcsok:
        if egy_gyumolcs.ar > legdragabb.ar:
            legdragabb = egy_gyumolcs
    return legdragabb

def random_gyumolcs(min_mennyiseg: int, max_mennyiseg: int = 100) -> gyumolcs:
    """
    Visszad egy véletlenszerű generált gyumolcs osztály példányt
    """

    # egy_random_gyumolcs = lehetseges_gyumolcsok[randint(0, len(lehetseges_gyumolcsok)-1)]
    egy_random_gyumolcs = choice(lehetseges_gyumolcsok)

    egy_gyumolcs = gyumolcs(egy_random_gyumolcs, randint(min_mennyiseg, max_mennyiseg), randint(300, 600))
    return egy_gyumolcs

def gyumolcsok_feltolt(mennyiseg: int) -> None:
    for i in range(mennyiseg):
        gyumolcsok.append(random_gyumolcs(100, 200))

def gyumolcsok_kiir() -> None:
    for egy_gyumolcs in gyumolcsok:
        print(f'{egy_gyumolcs.nev} - {egy_gyumolcs.mennyiseg} kg - {egy_gyumolcs.ar} Ft.') 

def teljes_keszlet_erteke() -> int:
    """
    Megszámolja és visszadja a gyümölcsben fekvő teljes pénzösszeget.
    """
    osszeg = 0
    for egy_gyumolcs in gyumolcsok:
        osszeg+= egy_gyumolcs * egy_gyumolcs.ar
    return osszeg