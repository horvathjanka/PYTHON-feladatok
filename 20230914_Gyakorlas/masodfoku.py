# Kérjük be egy másodfokú egyenlet együtthatóit (a, b, c), 
# és írjuk ki a gyökeit (megoldásait): x1, x2.

from math import sqrt

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

d = b**2 - 4 * a * c
if d >= 0:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(f'x1 = {x1}')
    print(f'x2 = {x2}')
else:
    print('Nincs megoldás a valós számok halmazán!')