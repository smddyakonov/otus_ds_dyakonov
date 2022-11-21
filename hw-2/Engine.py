"""Создайте датакласс Engine, добавьте атрибуты volume и pistons"""

from dataclasses import dataclass

@dataclass
class Engine:
    volume: float = 5.  # Объем двигателя
    pistons: str = '4T4R'  # Вид поршня, например, 4-ех тактный 4-ех рядный

    volume = volume
    pistons = pistons

"(2) В Engine не обязательно прописывать конструктор класса __init__. Декоратор @dataclass сам " \
"создаст конструктор (нужно только оставить инициализацию атрибутов типа book: str = 'name);"