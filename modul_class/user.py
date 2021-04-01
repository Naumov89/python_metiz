
class User():

    def __init__(self, first_name, last_name, user_country, user_city):
        self.first_name = first_name
        self.last_name = last_name
        self.user_country = user_country
        self.user_city = user_city
        self.login_attempts = 0

    def discribe_user(self):
        print(f"\tUser name: {self.first_name.title()}")
        print(f"\tLast name: {self.last_name.title()}")
        print(f"\tCountry: {self.user_country.title()}")
        print(f"\tCity: {self.user_city.title()}")

    def greet_user(self):
        print(f"Welcome {self.first_name.title()} {self.last_name.title()} to the site!")

    def quantity_users(self):
        print(f"Quantity: {self.login_attempts}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges():
    def __init__(self):
        self.privileges = ["allowed to delete users", "allowed to ban users", "allowed to add messages"]

    def show_privileges(self):
        print(f"Your privileges: {self.privileges}")
        

class Admin(User):
    def __init__(self, first_name, last_name, user_country, user_city):
        super().__init__(first_name, last_name, user_country, user_city)
        self.privileges = Privileges()