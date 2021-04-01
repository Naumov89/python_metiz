
class Restaurant():

    def __init__(self, restaurant_name, cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type

    def describe_restaurant(self):
        print(f"This is restaurant - {self.restaurant_name}.")
        print(f"Cusine type - {self.cusine_type}.")

    def open_restaurant(self):
        print("Restaurant is open!")


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cusine_type):
        super().__init__(restaurant_name, cusine_type)
        self.flavors = ['vanila', 'banana']

    def describe_flavors(self):
        print(f"Ice cream varieties: {self.flavors}")