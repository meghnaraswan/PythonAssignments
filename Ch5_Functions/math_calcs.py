#math examples

#area of circle
#area of triangle

import math

def circle(radius):
    '''Calculate the area of a circle''' #three air quaotations are used for commenting for functions
    return math.pi * radius ** 2

def trinagle(base, height):
    '''Calculate area of a triangle'''
    return (1/2) * base * height

def fact(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

print(circle(5))
print(trinagle(5, 3))
print(fact(5))
