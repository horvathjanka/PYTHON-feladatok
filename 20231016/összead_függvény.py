# Mit kell tudni egy függvényről ami nem mi írtunk:
# - mit csinál (függvény neve fontos)
# - mi a paraméter listája (A függvény neve után zárójelbgen megadott, vesszővel elválasztott változók)
#   - formális paraméterek (a függvény daklarációjakor zárójelben megadott változók, amiket a fgv. kap)
#   - aktuális paraméterek (a függvény hívásakor, a fgv-nek átadott értékek(lehet: kontans, változók, kifejezés...))
# - mit ad vissza  (return kulcsszó után megadott érték)
# - a függvény máltal visszadott érték behelyettesítődik a fgv. helyére.
# - a függvény a meghívásákor fut le, deklarációkor csak létrejön.

from random import randint

# def osszead(a, b): # a és b formális paraméterek. Ezeket fgv-en belül lehet használni.
def osszead(a: float, b: float) -> float:
    # print(a + b) # az eredmény nem kiírni szeretnénk, hanem visszaadni, ahogy egy randint() vagy egy eqrt() sem ír ki semmit
    return a + b
    # ami return mögött van az nem fut le.
    print('You should never see this')

# ezek mind valid kódok csak 'lógnak a levegőben' nincs semmi értelmük
osszead(2, 3) # 2 és a 3 - aktuális paraméter
randint(1, 10)
5
3 
34.5
# input('adj meg egy számot: ')
'alma'

x = float(input('Első szám:'))
y = float(input('Második szám:'))
print(f'{x} + {y} = {osszead(x, y)}') # x és y - aktuális paraméterek