#Create a class called Point with two members x, y both being integers.
#The class must contain a method called distance which can calculate the distance between two points. 
#Formula for the distance between two points =(x2 - y2).

# Import the math module to use the square root function.
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point):
        x = self.x - other_point.x
        y = self.y - other_point.y
        return math.sqrt(x**2+ y**2)
point1 = Point(1,2)
point2 = Point(4,6)

distance_between_points = point1.distance(point2)
print(f"The distance between the points is: {distance_between_points}")