# Döntsük el, hogy vehet-e alkoholt a vásárló avagy sem
# Elmúlt-e 18 éves

ma_ev = 2023
ma_honap = 9
ma_nap = 11

szuletes_ev = int(input('Születés éve: '))
if ma_ev - szuletes_ev < 18:
    print('Még nincs 18 éves. Nem vehet alkoholt!')
elif ma_ev - szuletes_ev > 18:
    print('Az alkohol öl butít és nyomorba dönt. Ha ezt akarja vehet alkoholt!')
else: # ==18
    szuletes_honap = int(input('Születési hónap: '))
    if ma_honap < szuletes_honap:
        print('Még nincs 18 éves, várjon pár hónapot. Nem vehet alkoholt!')
    elif ma_honap > szuletes_honap:
        print('Az alkohol öl butít és nyomorba dönt. Ha ezt akarja vehet alkoholt!')
    else:
        szuletes_nap = int(input('Születés napja: '))
        if ma_nap < szuletes_nap:
            print('Még nincs 18 éves, várjon pár napot. Nem vehet alkoholt!')
        elif ma_nap > szuletes_nap:
            print('Az alkohol öl butít és nyomorba dönt. Ha ezt akarja vehet alkoholt!')
        else:
            print('Boldog születésnapot. Tessék itt egy pohár pezsgő!')