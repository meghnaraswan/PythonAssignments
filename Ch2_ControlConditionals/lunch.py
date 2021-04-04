#lunch example

get_lunch = input("Do you want to have lunch with me today? (y/n) ")


#check if user wants to get lunch. y, n, or bad input
if get_lunch == 'y':
    print("Where do you want to eat?")
    print("1. Qdoba")
    print("2. Jamba Juice")
    print("3. Einstein Bagels")
    where_lunch = input("Enter the number of your choice: ")

    #check for what restaurant the user wants
    if where_lunch == '1' or where_lunch == '3': #user wants Qdoba
        print("Sounds great! Let's go!")

    elif where_lunch == '2': #user wants Jamba Juice
        print("No, thanks. Maybe next week.")

    #elif where_lunch == '3': #user wants Einstein Bagels
        #print("Sounds great! Let's go!")

    else:
        print("You did not give me a valid answer.")

elif get_lunch == 'n': #user says they don't want lunch
    print("Okay, maybe next week.")

else: #user gives bad input
    print("You did not give me a valid answer.")
