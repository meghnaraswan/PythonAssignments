#calculate area between two concentric circles

import math

#get user input
print("Calculate the area between two concentric circles.")
small_str = input("What is the radius of the smallest circle? ")
big_str = input("What is the radius of the biggest circle? ")

#convert varible to float
small_float = float(small_str)
big_float = float(big_str)

#calculate area
area_float = (big_float**2*math.pi) - (small_float**2*math.pi)

#report answer
print("Your area between the two concentric circle is: ", area_float)
