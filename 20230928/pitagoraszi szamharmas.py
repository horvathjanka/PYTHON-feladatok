# Pitagoraszi számhármasok

# A Pitagorasz-tétel azt mondja ki, hogy bármely derékszögű háromszög
# leghosszabb oldalának (átfogójának) négyzete megegyezik a másik két
# oldal (a befogók) négyzetének összegével. Röviden: a**2 + b**2 = c**2

# Írj programot, mely bekéri egy háromszög három oldalának hosszát, majd
# megállapítja, hogy a háromszög derékszögű-e! 
# A program várt működése pl. a következő:
# 1. oldal: 5 
# 2. oldal: 4 
# 3. oldal: 3 
# Derékszögű háromszög. 

# 1. oldal: 3
# 2. oldal: 6
# 3. oldal: 7
# Nem derékszögű háromszög

import math 

a = int(input('a oldal: '))
b = int(input('b oldal: '))
c = int(input('c oldal: '))


if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print('Derékszögű háromszög')
else:
    print('Nem derékszögű háromszög')
