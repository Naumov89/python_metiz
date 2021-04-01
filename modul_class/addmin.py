
from usser import User

class Privileges():
    def __init__(self):
        self.privileges = ["allowed to delete users", "allowed to ban users", "allowed to add messages"]

    def show_privileges(self):
        print(f"Your privileges: {self.privileges}")
        

class Admin(User):
    def __init__(self, first_name, last_name, user_country, user_city):
        super().__init__(first_name, last_name, user_country, user_city)
        self.privileges = Privileges()