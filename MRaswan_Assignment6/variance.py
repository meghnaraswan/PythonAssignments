#Meghna Raswan
#2337415
#raswan@chapman.edu
#CPSC 230-10 (1515)
#Assignment 6
#mean, variance, standard deviation

#start with an empty list
numbers = []
#assign number to 1
number = 1
while ( number > 0): #while loop for prompting user for positive integers since number is greater than 0
   number = int(input("Enter a number, then enter a negative number at the very end to stop: "))
   if number > 0:
       #save the number to use for later
       #stores integers into empty list above each time user inputs new integers
       numbers.append(number)

#sorting list in numerical order
def print_sorted(numbers):
    list_param = numbers[:] #copy-slice, assigning list_params the value of numbers withou changing value of numbers
    list_param.sort() #sorting list
    return list_param

#function for mean of the list
def compute_mean(numbers):
    return sum(numbers) / len(numbers) #taking the sum of the list and then dividing it by the length of the list

#function for variance of the list
def compute_variance(numbers, average):
   variance = 0
   for x in range(0, len(numbers)): #from 0 to however many numbers there are in the list
       variance += (average - numbers[x]) ** 2
   return variance / len(numbers) #the variance is the ((mean-the number at the first, all the way to the last index)^2)/(amount of numbers in the list)

#function for standard deviation of the list
def compute_std_dev(numbers, average):
    return compute_variance(numbers, average) ** (1/2) #calling the variance function; standard deviation is square root of variance

#printing list
print("Your list is:", numbers)

#sorted list
sorted_list = print_sorted(numbers)
print("Your list sorted is:", sorted_list)

#mean
mean = compute_mean(numbers)
print("The mean is:", mean)

#variance
variance = compute_variance(numbers, compute_mean(numbers))
print("The variance is:", variance)

#standard deviation
std_dev = compute_std_dev(numbers, compute_mean(numbers))
print("The standard deviation is:", std_dev)
