"""Набор классов для представления электромобилей"""

from car import Car

class Battery():
    """Простая модель аккумулятора электромобиля."""
    def __init__(self, battery_size=75):
        """Инициализирует атрибуты аккумулятора.""" 
        self.battery_size = battery_size

    def discribe_battery(self):
        """Выводит информацию о мощности аккамулятора."""
        print(f"This car has a {self.battery_size}- kWh battery.")

    def get_renge(self):
        """Выводит запас хода для аккумулятора."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """Класс потомок! Представляет аспекты машины, спкцефические для электромобилей."""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса родителя."""
        super().__init__(make, model, year) # super - функция которая вызивает метод родительского класса
        """Инициализирует атрибуты спецефические для электромобиля"""
        self.battery = Battery()
