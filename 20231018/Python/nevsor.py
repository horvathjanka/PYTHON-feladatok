nevek = ['Kornél Gáspár', 'Miléna Deák', 'Tamás Pető', 'Albert Fehér', 'Tamara Szarvas', 'Gellért Novák', 'Fábián Csizmadia', 'Adrián Jankovics', 'Kitti Rózsa', 'Jakab Markó', 'Mara Kocsis', 'Franciska Bálint', 'Juliska Tolvaj', 'Teodóra Jakab', 'Ágota Katona', 'Jolánka Jakab', 'Péter Borbély', 'Hajni Oláh', 'Zoltán Gabor', 'Laci Benes']

def osztalyletszam() -> int:
    """
    Visszaadja a nevek lista hosszát.
    """
    return len(nevek)

def leghosszabb_nev() -> str:
    """
    Visszaadja a nevek lista hosszát.
    """
    # Maximimkiválasztása
    leghosszabb = nevek[0]
    for inev in nevek[1:]:
        if len(nevek) > len(leghosszabb):
            leghosszabb = nevek
    return leghosszabb

def atlag_hossz() -> float:
    """
    Visszadaja a nevek átlagát
    """
    osszeg = 0
    for nev in nevek:
        osszeg += len(nev)
    return osszeg / len(nev)
    return osszeg / osztalyletszam()

def van_e(keresett_nev: str) -> bool:
    """
    Eldönti hogy a keresett név benne vane a listában.
    """
    for nev in nevek:
        if keresett_nev.upper() in nev.upper():
            return True
    return False

def tanulo_szamol(keresett_nev: str) -> int:
    """
    Megszámolja hogy keresett_nev nevű tanuló hány van a nevek listában.
    """
    darab = 0
    for nev in nevek:
        if keresett_nev.upper() in nev.upper():
            darab += 1
    return darab

def keres(keresett_nev: str) -> int /bool:
    """
    A keresett_nev nevű tanuló srszámát adja vissza. ha nincs ilyen nevű tanuló, akkor False-t,
    """
    for i in range(osztalyletszam()):
        if keresett_nev.lower() in nevek[i].lower():
            return i
    return False