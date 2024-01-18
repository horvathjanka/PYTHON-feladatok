from auto import auto

autok : list[auto] = []

def legerosebb():
    legnagyobb_teljesitmenyu_auto = autok(0)
    for a in autok:
        if a.teljesitmeny > legnagyobb_teljesitmenyu_auto.teljesitmeny:
            legnagyobb_teljesitmenyu_auto = a
    return leg

def autok_szin_alapjan(szin : str) -> list[auto]:
    autok_uj_listaja = []
    for a in autok:
        if a.szin.upper == szin.upper:
            autok_uj_listaja.append(a)
    return autok_uj_listaja


def auto_beker():
    rendszam = input('Az autó rendszáma: ')
    marka = input('Máraka: ')
    tipus = input('Típus: ')
    teljesitmeny = float(input('Teljesítmény (kW): '))
    szin = input('Színe: ')

    # eltároljuk a memóriában
    uj_auto = auto(rendszam, marka, tipus, teljesitmeny, szin)
    autok.append(uj_auto)
    
    #elmenjük fájlba
    file = open('autok.txt','a',encoding='utf8')
    file.write(rendszam+';'+marka+';'+tipus+';'+str(teljesitmeny)+';'+szin+'\n')
    file.close()

def autok_kiir(autok_listaja: list[auto]):
    for a in autok_listaja:
            print(f'{a.rendszam.ljust(10)} {a.marka.ljust(10)} {a.tipus.ljust(10)} {a.teljesitmeny:5.2f} {a.szin.ljust(10)}')

def autok_betolt():
    file = open('autok.txt','r',encoding='utf8')
    for sor in file:
        adatok = sor.strip().split(';')
        uj_auto = auto(adatok[0], adatok[1], adatok[2], float(adatok[3]), adatok[4])
        autok.append(uj_auto)
    file.close()