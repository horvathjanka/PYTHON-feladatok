
nevek = [BASTIEN Steven, dos SANTOS Felipe, DUBLER Cedric, ERM 
Johannes, HELCELET Adam Sebastian, KAZMIREK Kai, LEPAGE 
Pierce, MAYER Kevin, MOLONEY Ashley, ROE Martin, SCANTLING 
Garrett, SHKURENYOV Ilya, SYKORA Jiri, TILGA Karel, UIBO 
Maicel, URENA Jorge, VICTOR Lindon, WARNER Damian, 
WIESIOLEK Pawel, ZHUK Vitaliy, ZIEMEK Zachery]

idok = [8236, 7880, 7008, 8213, 8004, 8126, 8604, 8726, 8649, 7863, 8611, 
8413, 7943, 7018, 8037, 8322, 8414, 9018, 8176, 8131, 8435]


def versenyzokSzama():
    return len(nevek)

def legalabbDarab(limit):
    """"
    Visszaadja, hogy hány olyan versenyző volt ali legalább limit pontszámot ért el.
    """
    darab = 0
    for pont in idok:
        if pont > limit:
            darab += 1
    return darab

def atlag_pontszam() -> float:
    osszeg = 0
    for pont in idok:
        osszeg += pont
    return osszeg / len(idok)

def gyoztes_index() -> int:
    """
    vISSZADJA A GYŐZTES VERESENYZŐ INDEXÉT.
    """
    legtobb_indexe = 0
    for i in range(len(idok)):
        if idok[i] > idok[legtobb_indexe]:
            legtobb_indexe = i
    return legtobb_indexe

def gyoztes_index2() -> int:
    legtobb_indexe = 0
    legtobb_pont = idok[0]
    for i, pont in enumerate(idok):
        if pont > legtobb_pont:
            legtobb_pont = pont
    return legtobb_indexe

def gyoztes():
    """""
    Visszadja a győztes nevét
    """
    legtobb_indexe = 0
    legtobb_pont = idok[0]
    for i, pont in enumerate(idok):
        if pont > legtobb_pont:
            legtobb_pont = pont
    return legtobb_indexe

