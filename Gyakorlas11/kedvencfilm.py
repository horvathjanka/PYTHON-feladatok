def atvalt(hossz: int) -> []:
    ora = hossz // 60 # 73 perc -> 73 // 60 => 1
    perc = hossz % 60 # 73 °60 => 13
    return [ora, perc]

for i in range(3):
    cím =  input('Add meg a film címét!: ')
    hossz = int(input('Hány perces a film?'))
    ido = atvalt(hossz)
    print(f'A(z) {cím} című film {ido[0]} óra {ido[1]} perc hosszú.')
    