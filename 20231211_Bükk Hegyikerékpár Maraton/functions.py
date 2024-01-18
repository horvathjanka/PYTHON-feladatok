from versenytav import Versenytav

versenytavok : list[Versenytav]

def Beolvas(fajlnev: str):
    file = open(fajlnev, 'r', encoding='utf-8')
    file.readline()
    for sor in file:
        versenytavok.append(Versenytav(sor))
    file.close()

def CelbaerkezokAranya() -> float:
    return (1 - len(versenytavok) / 691) * 100

# megszámlálás
def Versenyzokszama(tav, nem):
    darab = 0
    for vt in versenytavok:
        if vt.Tav() == tav and vt.Nem() == nem:
            darab += 1
    return darab

# eldöntés
def VoltTobbMint(masodpercek):
    for vt in versenytavok:
        if vt.masodpercek > masodpercek:
            return True
    return False

# minimumkiválasztás
def AbszolutGyoztes() -> Versenytav:
    min = versenytavok[0]
    for vt in versenytavok:
        if vt.masodpercek < min.masodpercek:
            min = vt
    return min

def Gyoztes(tav, kategoria):
    min = 9999999999
    gyotesversenyzo = ''
    for vt in versenytavok:
        if tav == vt.tav and kategoria == vt.kategoria and vt.masodpercek < min:
            min = vt.masodpercek
            gyotesversenyzo = vt
    return gyotesversenyzo