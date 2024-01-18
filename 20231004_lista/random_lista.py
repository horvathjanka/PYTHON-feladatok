from random import randint

darab = int(input('Hány szám kell: '))

szamok = []

for i in range(darab):
    szamok.append(randint(10, 99)) # a lista végére beleteszi az elmeket

print(szamok)

# szamok.clear() # lista kiűritése
# print(szamok)

szamok.insert(0, 1) # az első paraméterbe megadott helyre beszúrja a 2. paraméterben megadott
print(szamok)

szam = szamok.pop() # A lista utolsó elemét kiveszi a listából és visszaadja
print(szam)
print(szamok)

szam = szamok.pop(0) # A lista 0. elemét kiveszi a listából és visszaadja
print(szam)
print(szamok)

torlendo = int(input('Mit szeretne törölni?: '))
szamok.remove(torlendo) # a megadott elem első előfordulását törli a listából
# ha nincs benne a listában az elem akkor hibaüzenetet kapunk

szamok.sor() # listát helyben rendezi
print(szamok) 

szamok.sor(reverse=True) #a listát helyben rendezi (csökkenőben)
print(szamok) 

masik_szamok = list(1, 2, 3, 4)
szamok.extend(masik_szamok) # a számok listához hozzáfűzi a másik_szamok listát
print(szamok)

meg_szamok = [9, 8, 7]
harmadik = masik_szamok