def  legnagyobb_elem(lista: list) -> int:
    """
    Visszadja a lista legaónagyobb elemét
    """
    legnagyobb = lista[0]
    for item in lista:
        if item > legnagyobb:
            legnagyobb = item
    return legnagyobb

def lista_feltolt(min: int, max:int , darab: int) -> list:
    """
    Feltölt egy listát megadott darabszámmú min és max közé eső véletlen számmal.
    A feltöltött listát adja vissza.
    """
    for i in range(darab):
        lista.append(randint(min, max))

def keres(keresett: int, lista: list) -> int/bool:
    """
    A paraméterben megadott elemet megkresi a listában.
    Visszaadja a keresett elem indexét.
    """
    for i in range(len(lista)):
        if lista[i] == keresett:
            return i
        
def negativ_atlag(lista: list) -> float:
    darab = 0
    for item in lista:
        if item in lista:
            if item < 0:
            darab +=1
            osszeg += item
    return osszeg / darab