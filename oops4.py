'''code to calculate the area of a circle by importing pi from math and create a class for circle
with a constructor,where radius is considerd as a arg
claculate and return the value to the object.'''

import math
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi * self.radius
r=int(input("Enter the radius:"))
c=circle(r)
print("Area of circle :",c.area())