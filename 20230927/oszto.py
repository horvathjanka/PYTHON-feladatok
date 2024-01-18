# Egy szám osztói

# Írj programot, mely bekér egy pozitív egész számot, majd kiszámolja és
# kiírja annak osztóit! Az osztók egy sorban, pontosvesszővel elválasztva
# jelenjenek meg!

# A program várt működése pl. a következő:
# Írj be egy pozitív egész számot: 15
# 15 osztói: 1; 3; 5; 15

szam = int(input('Írj be egy pozitív egész számot: '))
print(f'{szam} osztói: ', end= '')
for i in range(1, int(szam / 2)+ 1):
    
    if szam % i == 0:
        print(i, end=',')
print(szam)