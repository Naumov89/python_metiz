
def name_pet(name):
    pet = input("Are you have pet (y/n): ")
    if pet == 'y':
        pet_name = input("What name is your pet? ")
    else:
        pet_name = input("What would you like to name your pet? ")
    return pet_name.title()

