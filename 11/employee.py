
class Employee():

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, increase=5000):
        self.increase = increase
        self.salary += increase
        return self.salary

    def show_results(self):
        full_name = f"{self.first_name} {self.last_name} {self.salary}"
        return full_name

