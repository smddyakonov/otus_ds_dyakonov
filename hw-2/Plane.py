"""Создайте класс Plane

класс Plane должен быть наследником Vehicle
добавьте атрибуты cargo и max_cargo классу Plane
добавьте max_cargo в инициализатор (переопределите родительский)
объявите метод load_cargo, который принимает число, проверяет,
что в сумме с текущим cargo не будет перегруза, и обновляет значение, в ином случае
выкидывает исключение exceptions.CargoOverload
объявите метод remove_all_cargo, который обнуляет значение cargo и возвращает
значение cargo, которое было до обнуления
"""

import Vehicle
import exceptions

class Plane(Vehicle.Vehicle):
    cargo = 0     #"груз"
    max_cargo = 10

    def __init__(self, name, weight=Vehicle.Vehicle.weight, fuel=Vehicle.Vehicle.fuel,
                 fuel_consumption=Vehicle.Vehicle.fuel_consumption, cargo=cargo, max_cargo=None):
        super().__init__(name, weight, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo


    def load_cargo(self, load_cargo):
        cargo_tmp = self.cargo + load_cargo
        if cargo_tmp <= self.max_cargo:
            self.cargo = cargo_tmp
        else: raise exceptions.CargoOverload('Перегрузка груза')

    def remove_all_cargo(self):
        cargo_tmp = self.cargo
        self.cargo = 0
        print('обнулен cargo')
        self.cargo = cargo_tmp
        print('возвращано значение cargo')

        return f'{self.name} -> {cargo_tmp}'

"(3) В Plane методе remove_all_cargo под возвращением имеется ввиду return функции)) " \
"То есть созраняем вес в переменной, обнуляем его в атрибуте класса, затем return cargo_tmp."