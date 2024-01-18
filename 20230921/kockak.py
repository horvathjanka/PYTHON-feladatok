from random import randint

feldobasok_szama = int(input('Hány alkalommal legyen feldobás?'))

for i in range(feldobasok_szama):
dobas1 = randint(1, 6)
dobas2 = randint(1, 6)
dobas3 = randint(1, 6)
osszeg = dobas1 + dobas1 + dobas3
print(f'Dobás {dobas2} + {dobas2} = {dobas1} + {dobas2} + {dobas3} = {osszeg}', end=' ')
if osszeg < 10:
    print('Nyert: Panni')
else:
    print('Nyert: Anni')
    anni
    
print(f'A játék során{anni_nyert} alkalommal Anni, {feldobasok_szama - anni_nyert} alkalommal')