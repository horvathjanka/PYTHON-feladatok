from random import randint

mezo = -1

while mezo < 60:
    dobas = randint(1, 6)
    if mezo == -1:
        if dobas == 6:
            print('Dobás: 6 – Kilépett a start mezőre')
            mezo = 0
        else:
            print(f'Dobás: {dobas} – Nem léphet ki')
    else:
        if dobas + mezo < 60:
            print(f'Dobás: {dobas} – Aktuális mező: {mezo}')
            mezo += dobas
        elif dobas + mezo == 60:
            print(f'Dobás: {dobas} – Célba ért.')
            mezo += dobas
        else:
            print(f'Dobás: {dobas} – Nem léphet előre. Aktuális mező: {mezo}')
