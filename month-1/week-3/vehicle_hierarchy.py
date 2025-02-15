# Base class
class Vehicle:
    def __init__(self, make, model):
        self.make = make  # Car/Bike manufacturer
        self.model = model  # Model name

    def describe(self):
        return f"This is a {self.make} {self.model}."

# Subclass for Cars
class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)  # Call the parent class constructor
        self.num_doors = num_doors  # Number of doors in the car

    def describe(self):  # Overriding method
        return f"This is a {self.make} {self.model} with {self.num_doors} doors."

# Subclass for Bikes
class Bike(Vehicle):
    def __init__(self, make, model, bike_type):
        super().__init__(make, model)
        self.bike_type = bike_type  # Type of bike (e.g., sport, cruiser)

    def describe(self):  # Overriding method
        return f"This is a {self.make} {self.model}, which is a {self.bike_type} bike."

# Function to print vehicle details (Polymorphism)
def show_vehicle_info(vehicle):
    print(vehicle.describe())

# Creating objects
car1 = Car("Toyota", "Corolla", 4)
bike1 = Bike("Honda", "CBR500R", "Sport")

# Displaying information
show_vehicle_info(car1)
show_vehicle_info(bike1)
