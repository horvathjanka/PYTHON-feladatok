# növekményes ciklus - for

for i in range(10):
    # létrehoz egy i változót, 
    # amely felveszi a range fgv. által generál értékeket egymás után
    # ranege(10) -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    print('a')

for i in range(10, 20):
    print(i)

for i in range(100, 120, 2):
    print(i)

for i in range(200, 180, -2):
    print(i)

for i in range(2200, 2180, 2):
    # range üres tartományt ad -> egyszer sem fut le a ciklusmag (a ciklus belsejében lévő utasítások)
    print(i)

# KÉSŐBB: for lista elemein vagy fájl sorain is végig tud menni