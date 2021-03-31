##############################################################

# class Car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

# my_new_car = Car('audi', 'a4', 2020)
# print(my_new_car.get_descriptive_name())

##################################################################

# class Car():
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

# my_new_car = Car('audi', 'a4', 2020)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

#################################################################     1

# class Car():
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

# my_new_car = Car('audi', 'a4', 2020)
# print(my_new_car.get_descriptive_name())

# my_new_car.odometer_reading = 23    # izmenit znachenie
# my_new_car.read_odometer()

#####################################################################     2


# class Car():
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
#         self.odometer_reading = mileage

# my_new_car = Car('audi', 'a4', 2020)
# print(my_new_car.get_descriptive_name())

# my_new_car.update_odometer(24)   # izmenit znachenie
# my_new_car.read_odometer()

#######################################################################

# class Car():
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

# my_new_car = Car('audi', 'a4', 2020)
# print(my_new_car.get_descriptive_name())

# my_new_car.update_odometer(22)   # izmenit znachenie
# my_new_car.read_odometer()

###########################################################################       3

class Car():
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

my_used_car = Car('subaru', 'outback', 2017)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500) 
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

