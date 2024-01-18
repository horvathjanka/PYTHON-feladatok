ma_ev = 2023
ma_honap = 9
ma_nap = 11

szuletesi_datum = input('Születési dátum (éééé.hh.nn): ')
(szuletesi_ev, szuletesi_honap, szuletesi_nap) = szuletesi_datum.split('.')
szuletesi_ev = int(szuletesi_ev)
szuletesi_honap = int(szuletesi_honap)
szuletesi_nap = int(szuletesi_nap)

elmult_18 = False

if ma_ev - szuletesi_ev > 18:
    elmult_18 = True
elif ma_ev - szuletesi_ev == 18:
    if ma_honap > szuletesi_honap:
        elmult_18 = True
    elif ma_honap == szuletesi_honap:
        if ma_nap >= szuletesi_nap:
            elmult_18 = True

if elmult_18:
    print('Az alkohol öl butít és nyomorba dönt. Ha ezt akarja vehet alkoholt!')
else:
    print('Még nincs 18 éves. Nem vehet alkoholt!')
