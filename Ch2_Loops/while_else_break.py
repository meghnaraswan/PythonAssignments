import random #get the random number module
number = random.randint(0, 100)

print("Hi-Lo Number Guessing Game:between 0 and 100 inclusive")
print()

#get an initial guess
guess_str = input("Guess a number: ")
guess = int(guess_str) #convert str to number

#while guuess in range, keep asking
while 0 <= guess <= 100:
    if guess > number:
        print("Guessed too high.")
    elif guess < number:
        print("Guessed too low.")
    else: #correct guess, exit with break
        print("You guessed it! The number was:", number)
        break

    #keep going, get the next guess
    guess_str = input("Guess a number: ")
    guess = int(guess_str)
else:
    print("You quit early. the number was:", number)
