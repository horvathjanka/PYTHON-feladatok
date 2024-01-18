from cars import *

load_cars_from_file('autok.cvs')
print_cars_all_data()

# Hány autó szerepel a nyilvántartásban?
print(f'A nyilvántartásban {len(cars)} darab autó szerepel')

# Hány olyan auto van amely gyorsabb mint 200km/h.
print(f'{counter_cars_by_speed(200)} olyan auto van amely gyorsabb mint 200km/h-ra képes')

# Hány adott típusú autó (Suzuki) van a nyilvántartásban?
print(f'{counter_cars_by_brand("Suzuki")} Suzuki típusú autó van a nyilvántartásban')

# Mennyi a nyilvántartásban szereplő autók átlag fogyasztása?
print(f'A nyilvántartásban szereplő autók átlag fogyasztása {avg_consumption():.2f} 1/100km.')

#Mennyi a nyilvántartásban megadott típusú autók átlag ára?
print(f'Az Opel típusú autók átlagára: {avg_price_by_brand("Opel")}Ft.')

# Melyik a legdrágább autó?
print('A legdrágább autó adatai:')
most_expensive = most_expensive_car()
print(f'\tRendszáma: {most_expensive.PlateNumber}')
print(f'\tTípusa: {most_expensive.Brand}')
print(f'\tÁra: {most_expensive.Price}')

#Melyik a legnagyobb teljesítményű lada?
print('A legnagyobb teljesítményű Lada adatai:')
highest_HP = highest_HP_by_brand('Lada')
print(f'\tRendszáma: {highest_HP.PlateNumber}')
print(f'\tTeljesítménye: {highest_HP.HP}')
print(f'\tÁra: {highest_HP.Price}Ft')


