hetek = int(input('Hetek száma: '))
cel = float(input('Cél tömeg (kg): '))

elerte = -1
elozo = 0
novekedett = 0

for i in range(hetek):
    suly = float(input(f'{i + 1}. hét: '))
    if elerte == -1 and suly < cel:
        elerte = i
    if i == 0:
        elozo = suly
    else:
        if suly > elozo:
            novekedett += 1
        elozo = suly
    

print(f'Mari néni a {elerte + 1}. héten érte el először a kitűzött célt.')
print(f'A súlya {novekedett}-szer nőtt egyik hétről a másikra.')