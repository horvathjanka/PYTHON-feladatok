# Kérjük be egy kúp alapjának sugarát és magasságát (mindkettő valós szám)!
# Írjuk ki annak felszínét és térfogatát!

from math import sqrt, pow, pi

r = float(input('Adja meg a kúp sugarát!: '))
h = float(input('Adja meg a kúp magasságát!: '))

# a = sqrt(r**2 + h**2)
a = sqrt(pow(r, 2) + pow(h, 2))

A = round(pi * r**2 + pi * r * a, 2)
print(f'A kúp felszíne: {A}')

V = pi * r**2 * h / 3
# V = (pi * (r**2) * h) / 3
print(f'A kúp térfogata: {V:.2f}')


print(A)
print(V)