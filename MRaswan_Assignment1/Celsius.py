#Meghna Raswan
#2337415
#raswan@chapman.edu
#CPSC 230-10 (1515)
#Assignment 1
#convert Celsius to Fahrenheit

#get temperature in Celsius from user
Celsius_str = input("What is the temperature in Celsius? ")

#convert input to float
Celsius_float = float(Celsius_str)

#caculate temperature in Farenheit
Fahrenheit = Celsius_float * (9/5) + 32

#report the conversion to the user
print("The temperature in Fahrenheit is ", Fahrenheit)
