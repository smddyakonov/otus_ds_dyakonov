"""Создайте датакласс Engine, добавьте атрибуты volume и pistons"""

from dataclasses import dataclass

@dataclass
class Engine:
    volume: float = 5.  # Объем двигателя
    pistons: str = '4T4R'  # Вид поршня, например, 4-ех тактный 4-ех рядный

    def __init__(self, volume=volume, pistons=pistons):
        self.volume = volume
        self.pistons = pistons
