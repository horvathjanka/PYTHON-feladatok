#A bekérés ismétlődjön addig, amíg a név helyére '-' -et nem ír be a felhasználó.

nev = ''
while nev != '-':
   nev = input('Név ("-" = VÉGE): ')
   if nev != '-':
      osztaly = input('Osztály neve: ')
      kategoria = int(input('Kategória: '))
      koltseg = int(input('Költség: '))

      limit = kategoria * 10000

      if koltseg > limit:
          print(f'{nev}: {koltseg - limit} Ft')
      else:
          print(f'{nev}: nincs önköltség')
    







