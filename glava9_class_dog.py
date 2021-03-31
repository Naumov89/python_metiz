########################################################

# class Dog():
#     """Simple dog model!"""

#     def __init__(self, name, age):
#         """Initializes attributes name and age"""
#         self.name = name
#         self.age = age

#     def sit(self):
#         """The dog sits down on command"""
#         print(f'{self.name} is now sitting.')

#     def roll_over(self):
#         """The dog rolls on command"""
#         print(f"{self.name} rolled over!")


# my_dog = Dog('willie', 6)

# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")

# my_dog.sit()
# my_dog.roll_over()

###############################################################

class Dog():
    """Simple dog model!"""

    def __init__(self, name, age):
        """Initializes attributes name and age"""
        self.name = name
        self.age = age

    def sit(self):
        """The dog sits down on command"""
        print(f'{self.name.title()} is now sitting.')

    def roll_over(self):
        """The dog rolls on command"""
        print(f"{self.name.title()} rolled over!")


my_dog = Dog('willie', 6)
your_dog = Dog('rex', 4)

print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nMy dog's name is {your_dog.name.title()}.")
print(f"My dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()