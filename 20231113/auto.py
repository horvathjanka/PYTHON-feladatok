'''

class auto: # osztály
    tipus = '' # jellemzők, attribútomok
    rendszam = '' 
    szin = ''
    teljesitmeny =  0
'''

class auto:
    def __init__(self, tipus: str, rendszam: str, szin: str, teljesitmeny: float, gyorsulas: float) -> None:
    # metódus (az osztály saját függvényei)
    # példányosításkor fut le
    # self - hivatkozás a saját osztályra, minden metódus első paraméterre az kell legyen
    # gyorsulás - alapértelmezett értéke: 0 -> nem kötelező megadni
        self.tipus = tipus
        self.rendszam = rendszam
        self.szin = szin
        self.teljesitmeny = teljesitmeny
        self.gyorsulas = gyorsulas