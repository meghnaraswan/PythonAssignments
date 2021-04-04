#Meghna Raswan
#2337415
#raswan@chapman.edu
#CPSC 230-10 (1515)
#Assignment 2
#calculate the roots of the quadratic formula

import math

#get user input for a, b, and c
#convert input to float
a = float(input("What is the value of your 'a'? "))
b = float(input("What is the value of your 'b'? "))
c = float(input("What is the value of your 'c'? "))

#calculate the discriminant
discriminant = (b ** 2 - 4 * a * c)

#report the roots to the user if the discriminant is greater than or equal to 0
if discriminant >= 0:
    ##calculate the roots of the formula using the quadratic function
    quad1 = (- b + math.sqrt(discriminant)) / (2 * a)
    quad2 = (- b - math.sqrt(discriminant)) / (2 * a)
    print("The roots of this function is ", quad1, "and", quad2)
else: #inform the user that the roots cannot be determined since the discriminant is less than 0
    print("Sorry, this cannot be calculated since the discriminant is a negative value. "
          "Therefore, the quadratic equation has no real numbers.")
