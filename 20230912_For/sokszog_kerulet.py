# Kérjük be egy sokszög oldalainak számát!
# Kérjük be az oldalak hosszát!
# Írjuk ki a sokszög kerületét!

oldalak_szama = int(input('Adja meg a sokszög oldalainak számát!'))
kerulet = 0
for i in range(oldalak_szama):
    oldal_hossza = int(input('Adja meg az oldal hosszát!: '))
    # kerulet = kerulet + oldal_hossza
    kerulet += oldal_hossza # kerulet valtozo értékét növeljük meg az oldal_hosszával


print(f'A sokszög kerülete: {kerulet}')