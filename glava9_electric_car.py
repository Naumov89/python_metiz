############################################################

# class Car():
#     """Простая модель машины!"""
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading}")

#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")

#     def increment_odometer(self, miles):
#         self.odometer_reading += miles


# class ElectricCar(Car):
#     """Класс потомок! Представляет аспекты машины, спкцефические для электромобилей."""
#     def __init__(self, make, model, year):
#         """Инициализирует атрибуты класса родителя."""
#         super().__init__(make, model, year) # super - функция которая вызивает метод родительского класса


# my_car = Car('toyota', 'camry', 2015)
# print(my_car.get_descriptive_name())

# my_tesla = ElectricCar('tesla', 'models', 2019)
# print(my_tesla.get_descriptive_name())

#####################################################################################


class Car():
    """Простая модель машины!"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading}")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """Класс потомок! Представляет аспекты машины, спкцефические для электромобилей."""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса родителя."""
        super().__init__(make, model, year) # super - функция которая вызивает метод родительского класса
        """Инициализирует атрибуты спецефические для электромобиля"""
        self.batery_size = 75

    def discribe_battery(self):
        """Выводит информацию о мощности аккамулятора."""
        print(f"This car has a {self.batery_size}- kWh battery.")


my_tesla = ElectricCar('tesla', 'models', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.discribe_battery()
