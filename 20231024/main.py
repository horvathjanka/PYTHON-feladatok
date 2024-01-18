from távolugrás import print_egy_versenyzo, ugrasok_general, versenyzo_legjobb_ugrasa, gyoztes, ervenytelen_ugrasok_szama

eredmenyek = [] # minden versenyző legjobb eredmeny kerül bele

volt_legalabb_2_ervenytelen = False
for i in range(12):
    ugrasok = ugrasok_general()
    legjobb = versenyzo_legjobb_ugrasa(ugrasok)
    eredmenyek.append(legjobb)
    print_egy_versenyzo(i+1, ugrasok)
    if ervenytelen_ugrasok_szama(ugrasok) >= 3:
        volt_legalabb_2_ervenytelen = True

print(f'\nA győztes versenyző rajtszáma: {gyoztes(eredmenyek)}')

# Vane olyan versenyző akinek legalább 2 érvénytelen ugrás volt?
if volt_legalabb_2_ervenytelen:
    print('Van olyan versenyző, akinek legalább 2 érvénytelen ugrása volt.')
else:
    print('Nincs olyan versenyző, akinek legalább 2 érvénytelen ugrása volt.')