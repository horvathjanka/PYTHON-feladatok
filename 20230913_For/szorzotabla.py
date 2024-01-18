# Írjuk ki a 10*10-es szorzótáblát!

for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i * j:3d}', end=' ')
    print()