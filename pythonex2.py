#Create a class called Circle with two members x, y (center of the circle ) and rbeing the radius.
#The class must contain a methods called circumference and area compute them using the formulas circumference = 2*pi*r and area = pi * r2.

import math
class Circle:
        PI=3.142

        def __init__(self,radius):
                self.radius = radius
        def area (self):
                return (Circle.PI  * self.radius * self.radius)
        def circumference(self):
                return (2 * Circle.PI  * self.radius)
                
r = int(input("Enter the radius of circle:"))
c=Circle(r)
print ("Area of circle is:", c.area())   
print("Circumfernece of the Cirlce is:", c.circumference())
print("")
 
