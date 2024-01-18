# Kérjük be a számtani sorozat első elemét (a1), differenciáját (d), és elemszámát (n)!
# Írjuk ki a sorozat n darab elemét vesszővel elválasztva!

a1 = int(input('Kérem a sorozat első elemét: '))
d = int(input('Kérem a sorozat differenciáját: '))
n = int(input('Hány elemű legyen a sorzat?: '))

for i in range(n): # 0..n-1 -> i = 0, i = 1, i = 2 .. i = n-1
    an = a1 + i * d
    if i == n - 1:
        print(an, end=' ')
    else:
        print(an, end=', ')


# for i in range(1, n + 1):
#     an = a1 + (i - 1) * d
#     print(an, end=', ')