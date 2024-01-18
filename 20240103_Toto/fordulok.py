from fordulok import Fogadasi_fordulo

fordulok: list[Fogadasi_fordulo] = []

def beolvas(fajlnev):
    file = open(fajlnev)
    file = open(fajlnev, 'r', encoding='utf8')
    file.readline()
    for sor in file:
        fordulok.append(Fogadasi_fordulo(sor.strip()))
    file.close()

def teli_szelvenyek_szama():
    darab = 0
    for i in fordulok:
        darab += f.T13p1
    return darab

def volt_dontetlen_fordulo() -> bool:
    for f in fordulok:
        if f.volt_döntetlen() == False:
            return True
        return False
