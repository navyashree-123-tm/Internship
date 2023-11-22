class Animal:
    def __init__(self,name,method):
        self.name=name
        self.method=method

    def make_sound(self):
        print(self.sound)

class Bird(Animal):
    def make_sound(self):
        print("Chrip")

class Mammal(Animal):
    def make_sound(self):
        print("Roar")

class Parrot(Bird):
    def make_sound(self):
        print("Squak")

class Lion(Mammal):
    def make_sound(self):
        print("Growl")

parrot_instance=Parrot(name="Green Parrot", method="High Pitched")
lion_instance=Lion(name="African Lion", method="Deep")

parrot_instance.make_sound()
lion_instance.make_sound()


        