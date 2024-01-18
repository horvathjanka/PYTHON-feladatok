import math

szam = 363.81131

print(f'Egészre kerekítve: {round(szam)}')
print(f'Egy tizedesre kerekítve: {round(szam, 1)}')
print(f'Tizesekre kerekítve: {round(szam, -1)}')

print(f'Mindenképpen lefele kerekítve: {math.floor(szam)}')
print(f'Vagy lehet int fgv-nyel egésszé konvertálni (levágni a . utáni részt): {int(szam)}')

print(f'Mindenképpen felfele kerekítve: {math.ceil(szam)}')
