from nevsor import osztalyletszam, leghosszabb_nev, atlag_hossz, van_e, tanulo_szamol, keres

# Hány ember van az osztályban?
print(f'Az osztályban {osztalyletszam()} fő van.')


# Ki a leghosszabb nevű diák?
print(f'A leghosszabb nevű diák: {leghosszabb_nev()}')

# Átlagosan milyen hosszú egy név az osztályban?
print(f'Az osztályban átlagosan hosszú egy név: {atlag_hossz()}')

# Van-e az osztályban József?
# Ha van akkor hány?
# Ha van akkor hányadik a névsorban?
keresett = input('Kersesett tanuló neve:')
if van_e('József'):
    print(f'Van {keresett} az osztályban {tanulo_szamol(keresett)} fő.')
    print(f'A névsorban az első {keresett} sorszáma: {keres(keresett)}')
else:
    print(f'Nincs {keresett} az osztályban')

