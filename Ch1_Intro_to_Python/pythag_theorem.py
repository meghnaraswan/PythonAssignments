#calculate hypotenuse of right angle triangle

import math

#get user input
print("Calculate hypotenuse given the legs")
a_str = input("What is the first leg? ")
b_str = input("What is the second leg? ")

#convert variable to float
a_float = float(a_str)
b_float = float(b_str)

#calculate hypotenuse
c_float = math.sqrt(a_float**2 + b_float**2)

#report answer
print("The hypotenuse of a right angle with sides:", a_float, b_float)
print("hypotenuse:", c_float)
