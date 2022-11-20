import exceptions



from abc import ABC

class Vehicle(ABC):
    #weight = 1000  # масса
    started = False  # состояние started, False = not started True = started
    #fuel = 100  # топливо
    #fuel_consumption: int = 10  # потребление топлива

    def __init__(self, weight = 1000, fuel = 100, fuel_consumption = 12):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def get_var_names(self):
        """ получение имени переменной экзмепляра класса"""
        return [k for k, v in globals().items() if v is self]

    def __str__(self):
        """ вывод в print имени переменной экзмепляра класса"""
        return f'<{self.get_var_names()}>'

    def start(self):
        if self.started == False:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError('ошибка низкого уровня топлива (для старта)')

    def move(self):
        move_fuel = self.fuel - self.fuel_consumption
        if move_fuel > 0:
            self.fuel = move_fuel
        else:
            raise exceptions.NotEnoughFuel('Недостаточно топлива (для преодаления дистанции)')

print('test-1. Создание экземпляров')
car1 = Vehicle()
print(f'{car1}{[car1.weight, car1.started, car1.fuel, car1.fuel_consumption]}')
car2 = Vehicle(5000, 5, 12)
print(f'{car2}{[car2.weight, car2.started, car2.fuel, car2.fuel_consumption]}')
car3 = Vehicle(1200, 0, 12)
print(f'{car3}{[car3.weight, car3.started, car3.fuel, car3.fuel_consumption]}')
car4 = Vehicle(1200, 100, 12)
print(f'{car4}{[car4.weight, car4.started, car4.fuel, car4.fuel_consumption]}')

print('test-2. start')
try:
    car1.start()
except exceptions.LowFuelError as LFE:
    print(f'{car1}{[car1.weight, car1.started, car1.fuel, car1.fuel_consumption]} - {LFE}')
else:
    print(f'{car1}{[car1.weight, car1.started, car1.fuel, car1.fuel_consumption]}')

try:
    car2.start()
except exceptions.LowFuelError as LFE:
    print(f'{car2}{[car2.weight, car2.started, car2.fuel, car2.fuel_consumption]} - {LFE}')
else:
    print(f'{car2}{[car2.weight, car2.started, car2.fuel, car2.fuel_consumption]}')

try:
    car3.start()
except exceptions.LowFuelError as LFE:
    print(f'{car3}{[car3.weight, car3.started, car3.fuel, car3.fuel_consumption]} - {LFE}')
else:
    print(f'{car3}{[car3.weight, car3.started, car3.fuel, car3.fuel_consumption]}')

try:
    car4.start()
except exceptions.LowFuelError as LFE:
    print(f'{car4}{[car4.weight, car4.started, car4.fuel, car4.fuel_consumption]} - {LFE}')
else:
    print(f'{car4}{[car4.weight, car4.started, car4.fuel, car4.fuel_consumption]}')

print('test-3. move')
try:
    car1.move()
except exceptions.NotEnoughFuel as NEF:
    print(f'{car1}{[car1.weight, car1.started, car1.fuel, car1.fuel_consumption]} - {NEF}')
else:
    print(f'{car1}{[car1.weight, car1.started, car1.fuel, car1.fuel_consumption]}')

try:
    car2.move()
except exceptions.NotEnoughFuel as NEF:
    print(f'{car2}{[car2.weight, car2.started, car2.fuel, car2.fuel_consumption]} - {NEF}')
else:
    print(f'{car2}{[car2.weight, car2.started, car2.fuel, car2.fuel_consumption]}')

try:
    car3.move()
except exceptions.NotEnoughFuel as NEF:
    print(f'{car3}{[car3.weight, car3.started, car3.fuel, car3.fuel_consumption]} - {NEF}')
else:
    print(f'{car3}{[car3.weight, car3.started, car3.fuel, car3.fuel_consumption]}')

i=1
for i in range(9):
    try:
        car4.move()
    except exceptions.NotEnoughFuel as NEF:
        print(f'{car4}{[car4.weight, car4.started, car4.fuel, car4.fuel_consumption]} - {NEF}')
    else:
        print(f'{car4}{[car4.weight, car4.started, car4.fuel, car4.fuel_consumption]}')

