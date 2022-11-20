"""Cоздайте класс Car - класс Car должен быть наследником Vehicle -
добавьте атрибут engine классу Car - объявите метод set_engine, который принимает
в себя экземпляр объекта Engine и устанавливает на текущий экземпляр Car"""

import Vehicle
import Engine


class Car(Vehicle.Vehicle):
    engine = None


    def __str__(self):
        """Вывод в print, к выводу Vehicle добавлен атрибут engine"""
        return f'{self.name} -> {self.started, self.weight, self.fuel, self.fuel_consumption},' \
               f' {self.engine}'

    def set_engine(self, engine: Engine.Engine):
        self.engine = engine
