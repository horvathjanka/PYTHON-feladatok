from tanulok import *

tanulo1 = uj_tanulo()
print(f'{tanulo1.vezeteknev} {tanulo1.keresztnev} {tanulo1.szuletes}')

tanulok_feltolt(10)

tanulok[0].jegy_beir(5)
tanulok[9].jegy_beir(1)

tanulok_kiir()

legjobb_tanulo = osztaly_legjobbja

print(f'A legjobb tanuló: {legjobb_tanulo.vezeteknev} {legjobb_tanulo.keresztnev}. Átlaga: {legjobb_tanulo.atlag()}')
print(f'{osszatlag} tanulo van az osztályatlag folott')