'''code to calculate area and circumference of a circle by using a class rectangle,create a constructor and seperate functions for area
circ and delete the constructor , import math pi value'''
import math

class Rectangle:  
    def __init__(self, radius):
        self.radius = radius
        print(f"Constructor created with radius = {self.radius}")
    def area(self):
        return math.pi * self.radius ** 2
    def circumference(self):
        return 2 * math.pi * self.radius
    def delete(self):
        print("Deleting constructor...")
        del self.radius
circle = Rectangle(5)       
print("Area of circle:", circle.area())            
print("Circumference of circle:", circle.circumference())  
circle.delete() 