#suitcase at airport

checked_luggage_str = input("Do you have luggage to check? (y/n) ")

if checked_luggage_str == 'y':

    #get weight of suitcase
    weight_int = int(input("How much does your suitcase weigh (in pounds)? "))

    #check whether passenger owes $25 fee
    if weight_int >= 50:
        print("You owe us $25.")
    else:
        print("You owe us nothing!")
else:
    print("Lucky you!")

#Thank customer for their business
print("Thank you for your business!")
