#this program will add a series of positive integers and end twice once a negative is entered

#initialize variables
the_sum = 0

pos_num = True
while pos_num: #pos_num is our control variable
    num = int(input("Enter a number: ")) #get a number from the user
    if num > 0: #check value of input
        the_sum += num #running sum if positive
    else:
        pos_num = False #exit loop if negative
print("The total is", the_sum) #report answer to user
