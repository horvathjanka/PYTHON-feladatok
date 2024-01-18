from functions import Beolvas, CelbaerkezokAranya, Versenyzokszama, VoltTobbMint, AbszolutGyoztes

Beolvas('bukkm2019.txt')
print(f'Versenytávot nem teljesítők: {round(CelbaerkezokAranya(),2)}%.')
print(f'Versenytávot nem teljesítők: {CelbaerkezokAranya():.3}%.')
print(f'Rövod távon indult nők száma: {Versenyzokszama("Rövid", "Nő")}')
miniFerfi = Versenyzokszama("Mini", "Férfi")
print(f'Mini távon indult férfiak száma: {miniFerfi}')
if VoltTobbMint(6*60*60):
    print('Volt olyen versenyző aki, több mint 6 órán át volt a pályán.')
else:
    print('Nem volt olyen versenyző aki, több mint 6 órán át volt a pályán.')
gyoztes = AbszolutGyoztes("Rövid","ff")
print(f'A felnőtt férfi kategória győztese rövid távon: ')
print(f'\tRajtszám: {gyoztes.rajtszam}')
print(f'\tNév: {gyoztes.nev}')
print(f'\tEgyesület: {gyoztes.egyesulet}')
print(f'\tIdő: {gyoztes.ido}')
