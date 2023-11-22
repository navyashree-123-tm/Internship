class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)

    def area(self):
        return self.width * self.height

# Creating an instance of the Rectangle class with width 5 and height 10
my_rectangle = Rectangle(5, 10)

# Printing the area of the rectangle
print("Area of the rectangle:", my_rectangle.area())
