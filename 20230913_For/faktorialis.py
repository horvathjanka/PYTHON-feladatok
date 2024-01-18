# Kérjünk be egy számot, és írjuk ki a faktoriálisát!
# n! = 1*2*3*4*...*(n-1)*n

n = int(input('n = '))
faktorialis = 1
for i in range(2, n + 1):
    faktorialis *= i
    # faktorialis = faktorialis * i

print(f'{n}! = {faktorialis}')