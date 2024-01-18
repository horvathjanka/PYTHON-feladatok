# Készítsünk programot, amely bekér egy számot
# majd meghatározza, hogy az a szám négyzetszám-e!

from math import sqrt

szam = int(input('Kérek egy számot:' ))
gyok = sqrt(szam)
if gyok == round(gyok):
    print('Nem négyzetgyök')
else:
    print('Nem négyzetgyök')
    








