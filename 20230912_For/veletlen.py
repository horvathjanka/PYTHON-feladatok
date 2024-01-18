import random

for i in range(20):
    print(random.randint(2,10))
    # randint 2 paramétere benne van a lehetséges számok halmazában

x = random.random() # 0 <= x < 1
print(x)

# generáljuk egy random páros számot 0 és 100 között!
a = random.randrange(0, 101, 2)
print(a)