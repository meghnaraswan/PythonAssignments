# Write a program that prompts the user for a word
# and then calculates how many points that word would
# be worth in scrabble (points for each letter can
# need not check to see if the entry is a valid word
# nor account for point bonuses (a dictionary may be useful).

#dictionary to map letters to point values
points = {"a": 1 , "b": 3 , "c": 3 , "d": 2 ,
         "e": 1 , "f": 4 , "g": 2 , "h": 4 ,
         "i": 1 , "j": 8 , "k": 5 , "l": 1 ,
         "m": 3 , "n": 1 , "o": 1 , "p": 3 ,
         "q": 10, "r": 1 , "s": 1 , "t": 1 ,
         "u": 1 , "v": 4 , "w": 4 , "x": 8 ,
         "y": 4 , "z": 10}

#get user input
scrab_word = input("Enter a single word to score: ")
score = 0       #initialize score variable
for char in scrab_word.lower():     #loop over lowercase version of input
    score += points[char]           #add points for each letter

print('Your score is:',score)       #report score
