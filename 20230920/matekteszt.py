# Készítsunk programot, amely ki fogja kérdezni a matematikát
# (két szám összeadását, kivonását és szorzását <1,10> intervallumból )
# a két számot  és műveletet a számítógép  véletlenszerűen választja ki.
# Rossz válasz esetén kérdezze újra ugyanazt a példát.
# A program végén írjuk ki az eredményességét százalékokban.

from random import randint

KERDESEK_SZAMA = 5

# jovalaszok_szama = 0
# while jovalaszok_szama < 5
rossz_darab = 0
for i in range(KERDESEK_SZAMA):
    szam1 = randint(1, 10)
    szam2 = randint(1, 10)
    muvelet = randint(0, 2) # 0 = '+'    1 = '-'    2 = '*'
    
    helyes_valasz = False
    
    while helyes_valasz == False:
        match muvelet
          case  0: #'+'
            valasz = int(input(f'{szam1} + {szam2} = '))
            if szam1 + szam2 == valasz:
               print('Jó válasz')
               # jovalaszok_szama += 1
               helyes_valasz = 1
            else:
                 print('Rossz válasz')
                 rossz_valaszok_szama += 1
            case 1:
                valasz = int(input(f'{szam1} + {szam2} = '))
            if szam1 + szam2 == valasz:
               print('Jó válasz')
               # jovalaszok_szama += 1
               helyes_valasz = 1
                helyes_valasz = True
            case 2:
                valasz = int(input(f'{szam1} + {szam2} = '))
            if szam1 + szam2 == valasz:
               print('Jó válasz')
               # jovalaszok_szama += 1
               helyes_valasz = 1
                helyes_valasz = True
                
                 
print(f'Eredményesség: {KERDESEK_SZAMA/ (KERDESEK_SZAMA + rossz_valaszok_szama) *100:.2f}%')

# TODO: kb. ugyanazt csináltuk meg a 3 case-ben -> függvény
