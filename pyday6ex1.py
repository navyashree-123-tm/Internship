class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Creating an instance of the Dog class
my_dog = Dog()

# Calling the speak() method of the Dog class
my_dog.speak()
