class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def area(self):
        return 0.5 * self.width * self.height

# Creating instances of Rectangle and Triangle
my_rectangle = Rectangle(8, 4)
my_triangle = Triangle(6, 9)

# Printing the areas of the shapes
print("Area of the rectangle:", my_rectangle.area())
print("Area of the triangle:", my_triangle.area())
