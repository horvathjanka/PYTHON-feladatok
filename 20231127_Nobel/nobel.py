from dijazott import dijazott

dijazottak : list[dijazott] = []

def beolvas(fajlnev):
    fajl = open(fajlnev, 'r',encoding='utf8')
    fajl.readline()
    for sor in fajl:
        uj_dijazott = dijazott(sor.strip())
        dijazottak.append(uj_dijazott)
    fajl.close()

def tipusNevAlapjan(nev: str) -> str:
    for d in dijazottak:
        # teljesnev = d.keresztnev + " " + d.vezeteknev
        if nev.upper() == d.teljesnev.upper():
            return d.tipus
        return None

def dijazottEvEsTipusAlapjan(ev: int, tipus: str) -> dijazott:
    for d in dijazottak:
        if d.ev == ev and d.tipus == tipus:
            return d 
    return None

def szervezetekAdottEvUtan(ev: int) -> None:
    for d in dijazott:
        if d.ev >= ev and d.vezeteknev == '':
                print(f'{d.ev}: {d.keresztnev}')
        