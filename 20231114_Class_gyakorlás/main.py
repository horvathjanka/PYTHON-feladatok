from gyumolcs_kezeles import *

# gyumolcsok_feltolt(5)
random_gyumolcs2(100, 200)
print('Az üzlet gyümölcs készlete:')
gyumolcsok_kiir()

#Mennyi pénze van a teljes készletben az üzletnek?
print(f'\nA teljes készlet értéke: {teljes_keszlet_erteke()}Ft')

#Melyik a legdrágább gyümölcs?
legdragabb = legdragabb_gyumolcs()
print(f'A legdrágább gyümölcs: {legdragabb.nev}. Ára: {legdragabb.ar}Ft')

#Melyik gyümölcsben áll a legtöbb pénz?
print(f'A legtöbb pénz a {legtobb_penz_per_gyumolcs().nev} gyümölcsben áll.')