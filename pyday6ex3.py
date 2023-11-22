class Vehicle:
    def start_engine(self):
        print("Engine started")

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started")

# Creating instances of Car and Motorcycle
my_car = Car()
my_motorcycle = Motorcycle()

# Calling start_engine() method for both classes
my_car.start_engine()
my_motorcycle.start_engine()
