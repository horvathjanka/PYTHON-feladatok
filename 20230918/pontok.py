# Írjunk programot, amely bekéri a két pont kordinátáit,
# majd kiszámolja azok távolságát!
# P"(5,-3) - P1(x1,y1)
# P1(-4,3) - P2(x2,y2)

from random import sqrt

x1 = int(input('Az első pont x koordinátái: '))
y1 = int(input('Az első pont y koordinátái: '))
x2 = int(input('Az első pont x koordinátái: '))
y2 = int(input('Az első pont y koordinátái: '))

(x1-x2)**2 + (y1-2)**2

t= sqrt((x1-x2)**2 + (y1-y2)**2)
print(f 'A két pont közötti távolsága: {t}')