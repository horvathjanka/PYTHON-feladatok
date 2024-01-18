ora = -1
while ora != '':
    ora = -1
    while ora < 0 or ora > 23:
        ora_string = input('Hány óra van most? (ENTER-vége)')
        if ora_string != '':
            ora = int(ora_string)
            if ora >= 8 and ora < 16:
                print('A bolt nyitva van.')
                print('Ennyi órád van még odaérni: ', 16 - ora)
            else:
                print('A bolt zárva van.')
        else:
            ora = ora_string
            break

    