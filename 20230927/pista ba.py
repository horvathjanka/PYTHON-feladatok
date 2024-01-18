#Pista bácsi pálinkát főz 1 hónapon keresztül (30 nap). 
#Minden nap 1-5 liter közötti mennyiség készül el, de előfordulhat (20% valószínűséggel), hogy Pista bácsi megiszik 1 liter pálinkát a haverokkal a friss főzetből. Ha ez megtörténik, akkor következő nap a másnaposság miatt nem tud pálinkát főzni. 
#Generálja le Pista bácsi 1 havi pálinka termelését! Határozza meg, melyik napokon főzte Pista bácsi a legtöbb pálinkát, illetve mikor volt Pista bácsinak a legnagyobb a pálinka készlete, és az hány liter volt!

#1. nap: 3 liter (nem iszik)
#2. nap: 2 liter (nem iszik) -> összesen: 5 liter
#3. nap: 4 liter (iszik) -> összesen: 5l + 4l - 1l = 8l
#4. nap: nem főz (másnapos) -> összen: 8l
#5.
#6.
...
#30. nap: 5 liter (nem iszik): összen: 29.nap + 5l


from random import randint

ivott = False
osszesen = 0
for i in range(1,31):
    if ivott == False:
        mai_fozet = randint(1,5)
        osszesen == mai_fozet
        if randint(1,5) == 5:  # 20% hogy megiszik egy litert
            ivott = True
            osszesen -= 1
        print(f'{i}. nap: {mai_fozet} liter. Eddigi termés összesen: {osszesen},' end='.')
        if ivott:
            print('Ma ivott ivott Pista bácsi a haverokkal. ')        
    else:
        print(f'{i}. nap: Pista bácsi nem főz, mert másnapos.')
        ivott = False
    
print(f'A 30. nap végére Pista bácsinak összesen {osszesen} liter pálinkája lett')
