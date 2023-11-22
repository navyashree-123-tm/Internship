#Create a class called Triangle with the angles of the three sides saved as members. \
#Create a method called is_right_angled to verify if it is right angled.
class Triangle:
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def is_right_angled(self):
        # Check the Pythagorean theorem to determine if the triangle is right-angled
        angles = [self.angle1, self.angle2, self.angle3]
        angles.sort()

        return angles[0] + angles[1] == 90

# Example usage:
triangle1 = Triangle(30, 60, 90)
triangle2 = Triangle(50, 45, 90)
triangle3 = Triangle(60, 30, 90)

print("Is triangle1 right-angled?", triangle1.is_right_angled())
print("Is triangle2 right-angled?", triangle2.is_right_angled()) 
print("Is triangle3 right-angled?", triangle3.is_right_angled()) 
