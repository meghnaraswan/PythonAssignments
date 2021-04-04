#Meghna Raswan
#2337415
#raswan@chapman.edu
#CPSC 230-10 (1515)
#Assignment 1
#calculate the roots of the quadratic formula

import math

#get user input for a, b, and c
a_str = input("What is the value of your 'a'? ")
b_str = input("What is the value of your 'b'? ")
c_str = input("What is the value of your 'c'? ")

#convert input to float
a_float = float(a_str)
b_float = float(b_str)
c_float = float(c_str)

#quadratic function
#function = a_float * print("x")**2 + b_float * print("x") + c_float

#calculate the roots of the formula
quad1 = (- b_float + math.sqrt(b_float**2 - 4 * a_float * c_float))/(2 * a_float)
quad2 = (- b_float - math.sqrt(b_float**2 - 4 * a_float * c_float))/(2 * a_float)

#report the roots to the user
print("The roots of this function is ", quad1, "and", quad2)
