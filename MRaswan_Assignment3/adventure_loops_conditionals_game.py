#Meghna Raswan
#2337415
#raswan@chapman.edu
#CPSC 230-10 (1515)
#Assignment 3
#Choose Your Own Adventure

import random
#variable creation & setting loop control variable

room = 1

#generating a random number
death_die = random.randint(1, 100)

while room != 0: #while loop for when room is not equal to 0; none of the rooms are assigned 0
    if room == 1: #room 1 is hallway
        print("You have now entered this mysterious castle and are now in the hallway. Your goal is to find the "
              "hidden treasure. There is doorway to the 'living room', 'dining hall', 'bed chambers', and 'kitchen'.")
        choice = input("Which room would you like to choose? ")
        #these are all of the choices from whn you are in the hallway
        if choice == 'living room':
            room = 2
        elif choice == 'dining hall':
            room = 3
        elif choice == 'bed chambers':
            room = 4
        elif choice == 'kitchen':
            room = 5
        else: #if the choice is none of the rooms
            print(choice, " wasn't one of the options. Try again.")
    #section for choosing 'living room'
    elif room == 2:
        if death_die > 50: #there is a 50% chance that the player will die by ghosts, using the random integer generator indicated in the beginning
            print("You tragically died by the haunting ghosts.")
            room = 0
        else:
            room = 2
            print("You have entered the living room, successfully avoiding the haunted ghosts. There is a doorway "
                  "to either the 'dining hall' or a 'secret passageway'.")
            choice = input("Which room would you like to choose? ")
            if choice == 'dining hall':
                room = 3
            elif choice == 'secret passageway':
                room = 9
            else:
                print(choice, " wasn't one of the options. Please try again.")
    #section for choosing 'dining hall'
    elif room == 3:
        print("You have just entered the dining hall. There is a doorway to either the 'lavatory' or 'living room'.")
        choice = input("Which room would you like to choose? ")
        if choice == 'lavatory':
            if death_die > 50: #there is a 50% chance that the player will die by zombies
                print("You suffered an awful death by brain-eating zombies.")
                room = 0
            else:
                print("You successfully avoided the brain-eating zombies. But, you have reached a 'dead' end.")
                choice = input("Please write 'back' to go back. ")
                if choice == "back":
                    room = 3
                else:
                    print(choice, " wasn't one of the options. Please try again.")
        elif choice == 'living room':
            room = 2
        else:
            print(choice, " wasn't one of the options. Please try again.")
    #section for choosing 'bed chambers'
    elif room == 4:
        print("You have reached a 'dead' end.")
        choice = input("Please write 'back' to go back. ")
        if choice == "back":
            room = 1
    #section for choosing 'kitchen'
    elif room == 5:
        print("You have just entered the kitchen. There is a doorway to the 'garden' and 'secret passageway'.")
        choice = input("Which room would you like to choose? ")
        if choice == 'garden':
            if death_die > 50: #there is a 50% chance that the player will die by monsters
                print("You were trampled by many monsters.")
                room = 0
            else:
                room = 7
                print("You have entered the garden, successfully avoiding the monsters. There is a doorway "
                      "to either the 'secret passageway'.")
                choice = input("Open the doorway to the secret passageway by typing 'secret passageway'? ")
                if choice == 'secret passageway':
                    room = 9
                else:
                    print(choice, " wasn't one of the options. Please try again.")
        elif choice == 'secret passageway':
            room = 9
        else:
            print(choice, " wasn't one of the options. Please try again.")
    #section for choosing 'secret passageway'
    elif room == 9:
        print("You have entered a secret passageway. This passageway can lead you to the 'living room', "
              "\'basement', or 'kitchen'.")
        choice = input("Which room would you like to choose? ")
        if choice == 'living room':
            room = 2
        elif choice == 'basement':
            room = 10
        elif choice == 'kitchen':
            room = 5
        else:
            print(choice, " wasn't one of the options. Please try again.")
    #section for choosing 'basement'
    #user is informed that they have found the treasure
    elif room == 10:
        print("Yay! You have successfully found the treasure!")
        room = 0


