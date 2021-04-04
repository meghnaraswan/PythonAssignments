#functions calling functions

import math

def circle(radius):
    '''Calculate the area of a circle'''
    return math.pi * radius ** 2

def cylinder(radius, height):
    '''Calculate the volume of a cylinder'''
    return circle(radius) * height

print(circle(5))
print(cylinder(2, 5))
