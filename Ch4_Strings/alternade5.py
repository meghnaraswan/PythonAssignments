#Meghna Raswan
#2337415
#raswan@chapman.edu
#CPSC 230-10 (1515)
#Assignment 4
#alternade

import string

option = 1

while option != 0: #while loop for when option is not equal to 0; none of the options are assigned 0
    if option == 1: #option 1 is choosing either destruct or construct
        print("Would you like to destruct an alternade or construct 2 words from a alternade?")
        #get user input
        choice_str = input("Please enter either 'destruct' or 'construct': ")
        if choice_str == "destruct":
            option = 2
        elif choice_str == "construct":
            option = 3
        else:
            print(choice_str, "was an invalid answer. Please try again.")

    #when user inputs 'destruct'
    elif option == 2:
        if choice_str == "destruct":
            original_str = input("Enter an alternade: ")

            #make string lowercase
            modified_str = original_str.lower()

            #remove punctuation and whitespace
            bad_chars = string.punctuation + string.whitespace

            for char in bad_chars: #iterate over bad character string
                modified_str = modified_str.replace(char, "")

            original_txt = original_str.isalpha()

            #alternade visualization
            if original_str.isalpha():

                #shows original string
                print("The original string is: " + original_str)

                #shows modified string after removing puntuation, whitespace, and making it lowercase
                print("The modified string is: " + modified_str)

                #1st alternade starting from 0 (1st place of word) and counting up the word by 2
                print("Word 1 is: " + modified_str[::2])

                #determining if length is odd or even
                if len(modified_str[::2]) % 2 == 0: #if remainder of length of word is 0, word is even
                    print("The first word has an even length.")
                elif len(modified_str[::2]) % 2 == 1: #if remainder of length of word is 1, word is odd
                    print("The first word has an odd length.")
                else:
                    print("This is an invalid input")

                #2nd alternade starting from 1 (2nd place of word) and counting up the word by 2
                print("Word 2 is: " + modified_str[1::2])

                #determining if length is odd or even
                if len(modified_str[1::2]) % 2 == 0: #if remainder of length of word is 0, word is even
                    print("The second word has an even length.")
                elif len(modified_str[1::2]) % 2 == 1: #if remainder of length of word is 1, word is odd
                    print("The second word has an odd length.")
                else:
                    print(choice_str, "was an invalid answer. Please try again.")
                option = 0

            while original_txt != True:
                print("Please enter only alpha characters.")
                original_str = input("Enter an alternade: ")
                original_txt = original_str.isalpha()
        else:
            print(choice_str, "was an invalid answer. Please try again.")

    #when user inputs 'construct'
    elif option == 3:
        if choice_str == "construct":
            first_str = input("Enter the first word: ")
            second_str = input("Enter the second word: ")

            #make first and second string lowercase
            first_str = first_str.lower()
            second_str = second_str.lower()

            first_txt = first_str.isalpha()
            second_txt = second_str.isalpha()

            alternade = ""
            y = 0
            x = 0

            #check to see if string has no punctuation, numbers, or spaces
            if first_str.isalpha() and second_str.isalpha():
                #if the length of first word is greater than the length of second word (result alternade will have an odd length)
                if len(first_str) > len(second_str):
                    #while loop will create first even letters, alternating the letters of each word until the last letter of first word
                    while y < (len(first_str) - 1):
                        alternade = alternade + first_str[y].upper() + second_str[x] #.upper will make every alternating letter starting from the first letter uppercase (except for last letter)
                        x += 1
                        y += 1
                    #if statement will add last letter of first word
                    if x > (len(second_str) - 1):
                        alternade = alternade + first_str[y].upper() #.upper will make last letter uppercase

                    print("The alternade is:", alternade)

                    #determining if length is odd or even (which will be odd regarless)
                    if len(alternade) % 2 == 0:
                        print("The word has an even length.")
                    elif len(alternade) % 2 == 1:
                        print("The word has an odd length.")
                    else:
                        print(choice_str, "was an invalid answer. Please try again.")
                    option = 0

                #if the length of first word is less than the length of second word (result alternade will have an odd length)
                elif len(first_str) < len(second_str):
                    #while loop will create first even letters, alternating the letters of each word until the last letter of last word
                    while x < (len(second_str) - 1):
                        alternade = alternade + second_str[x].upper() + first_str[y] #.upper will make every alternating letter starting from the first letter uppercase (except for last letter)
                        x += 1
                        y += 1
                    #if statement will add last letter of last word
                    if y > (len(first_str) - 1):
                        alternade = alternade + second_str[y].upper() #.upper will make last letter uppercase

                    #determining if length is odd or even (which will be odd regarless)
                    print("The alternade is:", alternade)
                    if len(alternade) % 2 == 0:
                        print("The word has an even length.")
                    elif len(alternade) % 2 == 1:
                        print("The word has an odd length.")
                    else:
                        print(choice_str, "was an invalid answer. Please try again.")
                    option = 0

                #if the length of the first and last word is the same (result alternade will have an even length)
                elif len(first_str) == len(second_str):
                    for z in first_str:
                        alternade = alternade + z.upper() + second_str[y] #.upper will make every alternating letter starting from the first letter uppercase
                        y += 1
                    print("The alternade is:", alternade)

                #determining if length is odd or even (which will be even regarless)
                    if len(alternade) % 2 == 0:
                        print("The word has an even length.")
                    elif len(alternade) % 2 == 1:
                        print("The word has an odd length.")
                    else:
                        print(choice_str, "was an invalid answer. Please try again.")
                    option = 0

                else:
                    print(choice_str, "was an invalid answer. Please try again.")
            while first_txt and second_txt != True:
                print("Please enter only alpha characters.")
                first_str = input("Enter the first word: ")
                second_str = input("Enter the second word: ")
                first_txt = first_str.isalpha()
                second_txt = second_str.isalpha()

        else:
            print(choice_str, "was an invalid answer. Please try again.")

    #if user wrote something other than 'destruct' or 'construct'
