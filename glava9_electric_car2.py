###########################################################

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



my_tesla = ElectricCar('tesla', 'models', 2019)

print(my_tesla.get_descriptive_name())

my_tesla.battery.discribe_battery()
my_tesla.battery.get_renge()



