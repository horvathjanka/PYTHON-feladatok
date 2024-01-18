nev = 'Béla'
print(type(nev))
szam = 1.1 #deklaráció (definició -> kezdőértéket is kapott) -Y először használjuk
# a változó a deklaráció után használható
# csak az öt deklaráció blokkban érvényes
print(type(szam))
szam = '2'
print(type(szam))

a = input('Adjon meg egy számot:')
b = input('Adjon meg mégegy számot:')
print('Összefűzve:', a + b)
print(float(a) + float(b))
print(a,'+',b,'-',float(a) + float(b))
print(f'{a} + {b} = {float(a) + float(b)}')

# komment - Ctrl+K+C


# white space -> szóköz, tabulátor, enter
print(alma) # unexpected indentation

'''     print('alma) '''


vezetek_nev = 'Kovács' # snake case
vezeteknev = 'Kiss' #camel case
vezetekNev = 'Takács' # Pascal case
