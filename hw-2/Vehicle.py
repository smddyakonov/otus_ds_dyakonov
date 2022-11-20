"""Доработайте базовый класс Vehicle:

добавьте атрибуты weight, started, fuel, fuel_consumption со значениями по умолчанию
добавьте инициализатор для установки weight, fuel, fuel_consumption
добавьте метод start, который, если ещё не состояние started, проверяет, что топлива
больше нуля, и обновляет состояние started, иначе выкидывает исключение exceptions.LowFuelError
добавьте метод move, который проверяет, что достаточно топлива для преодоления переданной
дистанции, и изменяет количество оставшегося топлива, иначе выкидывает исключение
exceptions.NotEnoughFuel"""

import exceptions

from abc import ABC


class Vehicle(ABC):
    weight = 1000  # масса
    started = False  # состояние started, False = not started or True = started
    fuel = 100  # топливо
    fuel_consumption = 10  # потребление топлива

    def __init__(self, name, weight=weight, fuel=fuel, fuel_consumption=fuel_consumption):
        """Инициализатор"""
        self.name = name
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def __str__(self):
        """Вывод в print"""
        return f'{self.name} -> {self.started, self.weight, self.fuel, self.fuel_consumption}'

    def start(self):
        """Метод start"""
        if self.started == False:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError('ошибка низкого уровня топлива (для старта)')
        return self.name, self.started

    def move(self):
        """Метод move"""
        move_fuel = self.fuel - self.fuel_consumption
        if move_fuel >= 0:
            self.fuel = move_fuel
        else:
            raise exceptions.NotEnoughFuel('Недостаточно топлива (для преодаления дистанции)')
        return self.name, self.fuel

    def stop(self):
        """Метод stop (переводит start  = True в start  = False"""
        if self.started == True:
            self.started = False