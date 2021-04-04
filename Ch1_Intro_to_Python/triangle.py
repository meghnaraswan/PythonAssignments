#calculate the area of a triangle
#Meghna Raswan
#CPSC 230

#Calculate the area of a triangle based on user input

#Get the base and height of a triangle from the user
base_str = input("What is the base of the triangle? ")
height_str = input("What is the height of the triangle? ")

#convert inputs to float
base_float = float(base_str)
height_float = float(height_str)

#claculate the area of the triangle
area = 0.5 * base_float * height_float

#Report the area to the user
print("The area of the triangle is", area)
