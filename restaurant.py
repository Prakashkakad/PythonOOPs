class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        print("Available Ice Cream Flavors:")
        for flavor in self.flavors:
            print("- " + flavor)

# Create an instance of IceCreamStand
ice_cream_stand = IceCreamStand("Scoops Ahoy", "Ice Cream Parlor")
ice_cream_stand.flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint Chocolate Chip']

# Display the ice cream flavors
ice_cream_stand.display_flavors()