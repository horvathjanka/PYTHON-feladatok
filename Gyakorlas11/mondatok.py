from random import choice

def nevelo(fonev: str) -> str:
    magangzok = 'öüóeuioőúaéáűí'

    if fonev[0].upper() in magangzok.upper():
        return 'Az'
    else:
        return 'A'

def jelzo() -> str:
    jelzok = ['könnyed', 'piros', 'nagy']
    return choice(jelzok)

print('Adj meg három főnevet!')
for i in range(3):
    fonev = input(f'{i+1} főnév:')
    print(f'{nevelo(fonev)} {fonev} {jelzo()}.')