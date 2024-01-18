from random import randint

# print(2,3,4,5, sep=' - ')
# print(2,3,4,5, sep=', ')

# Lottó: 5/90
# TODO: egyelőre nem tudjuk megoldani, hogy ne ismétlődjön
print('Az ötöslottó e heti nyerőszámai: ', end='')
for i in range(5):
    print(randint(1,90), end=' ')

# 6-os lottó: 6/45
print('A hatoslottó e heti nyerőszámai: ', end='')
# for i in range(6):
# for i in range(1,7):
# for i in range(0,6):
for i in range(0,6,1):
    print(randint(1,45), end=' ')