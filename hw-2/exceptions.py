"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    """ошибка низкого уровня топлива (для старта)"""

class NotEnoughFuel(Exception):
    """Недостаточно топлива (для преодаления дистанции)"""

class CargoOverload(Exception):
    """Перегрузка груза"""