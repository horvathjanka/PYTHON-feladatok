def sikeres (pontszam: int) -> bool:
    return pontszam > 48

while True:
    nev = input('Add meg a vizsgázó nevét!')
    if nev == '':
        break
    pontszam = int(input('Add meg a pontszámát: '))
    if sikeres(pontszam):
        print(f'{nev} vizsgája sikeres.')
    else:
        print(f'{nev} vizsgája sikertelen.')