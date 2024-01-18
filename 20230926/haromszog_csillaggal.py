
oldal_hossza = int(input('A háromszög oldalának hossza: '))

for i in range(oldal_hossza):
    for j in range(i):
        print('*', end='')
    print()
    
for i in range(oldal_hossza):
    for j in range(oldal_hossza-i):
        print('*', end='')
    print()
    
    
