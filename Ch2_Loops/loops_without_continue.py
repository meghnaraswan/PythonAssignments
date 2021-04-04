#sum up a series of even numbers
#make sure input is only even numbers

print("Allow the user to enter a series of even integers. Sum them.")
print("Ignore non-even input. End with a '.'")
#initialize the input number and sum

number_str = input("Number: ")
the_sum = 0

while number_str != ".": #end loop on '.' character
    number = int(number_str)
    if number % 2 == 1:
        pass
    else:
        the_sum += number
    number_str = input("Number: ")

print("The sum is:", the_sum)

    #pass #do something
    #print ("Error, only even numbers please.")
    #number_str = input(Number: ")