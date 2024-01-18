from car import car

cars : list[car] = []

def highest_HP_by_brand(brand : str) -> car:
    highest_HP = -1
    highest_HP_car = None
    for c in cars:
        if c.Brand == brand and c.HP > highest_HP:
            highest_HP = c.HP
            highest_HP_car = c
        return highest_HP_car

def avg_price_by_brand(brand: str) -> float:
    sum_price = 0
    counter = 0
    for c in cars:
        if c.Brand == brand:
            sum_price += c.Price
            counter += 1
        return sum_price / counter

def most_expensive_car() -> car:
    most_expensive = cars[0]
    for c in cars:
        if c.Price > most_expensive.Price:
            most_expensive = c
    return most_expensive

def load_cars_from_file(filename: str) -> None:
    file = open(filename, 'r', encoding='utf8')
    file.readline()
    for row in file:
        # new_car = car(row)
        # cars.append(new_car) 
        cars.append(car(row))
    file.close()

def print_cars_all_data() -> None:
    for c in cars:
        print(f'{c.PlateNumber} - {c.Brand} - {c.Cm3}cm3 - {c.Price}Ft')

def counter_cars_by_speed(speed: int) -> int:
    """
    Megszámolja hány olyan auto van amelynek a végsebessege eléri a megadott speed-et.
    """
    counter = 0
    for c in cars:
        if c.Speed > speed:
            counter += 1
    return counter

def counter_cars_by_brand(brand: str) -> int:
    """
    Megszámolja hány brand típusú autó van.
    """
    counter = 0
    for c in cars:
        if c.Brand == brand:
            counter += 1
    return counter

def avg_consumption() -> float:
    sum_consumption = 0
    for c in cars:
        sum_consumption += c.Consumption
    return sum_consumption / len(cars)