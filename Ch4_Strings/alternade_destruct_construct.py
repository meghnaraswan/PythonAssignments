#Meghna Raswan
#2337415
#raswan@chapman.edu
#CPSC 230-10 (1515)
#Assignment 4
#alternade

import string

print("Would you like to destruct an alternade or construct 2 words from a alternade?")

#get user input
choice_str = input("Please enter either 'destruct or 'construct': ")

#when user inputs 'destruct'
if choice_str == "destruct":
    original_str = input("Enter an alternade: ")

    #make string lowercase
    modified_str = original_str.lower()

    #remove punctuation and whitespace
    bad_chars = string.punctuation + string.whitespace

    for char in bad_chars: #iterate over bad character string
        modified_str = modified_str.replace(char, "")

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
            print("This is an invalid input")

    else:
        print("This is an invalid input")

#when user inputs 'construct'
elif choice_str == "construct":
    first_str = input("Enter the first word: ")
    second_str = input("Enter the second word: ")

    alternade = ""
    y = 0
    x = 0

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

        #determining if length is odd or even (which will be odd regarless)
        print("The alternade is:", alternade)
        if len(alternade) % 2 == 0:
            print("The word has an even length.")
        elif len(alternade) % 2 == 1:
            print("The word has an odd length.")
        else:
            print("This is an invalid input")
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

    #if the length of the first and last word is the same (result alternade will have an even length)
    else:
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
            print("This is an invalid input")

#if user wrote something other than 'destruct' or 'construct'
else:
    print("This is an invalid input")
