
'''Класс для представления автомобиля'''

class Car():
    """Инициализирует атрибуты описания автомобиля"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег в миях"""
        print(f"This car has {self.odometer_reading}")

    def update_odometer(self, mileage):
        """
        Устанавливает на одометре заданное значение.
        При попытке обратной прокрутки изменение отклоняеться.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Увеличивает показания одометра с заданным приращением"""
        self.odometer_reading += miles