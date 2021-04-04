#Meghna Raswan
#2337415
#raswan@chapman.edu
#CPSC 230-10 (1515)
#Assignment 4
#pig latin

def word_to_pig(word):
    latin = ""
    vowels = "aeiou"
    first = word[0]
    if first in vowels:
        word += 'yay'
    else:
        x = word[1::] + word[0]
        x += 'ay'
        word = x
    latin = word
    return latin

def name_to_pig(name):
    list = name.split()
    first = list[0].lower()
    last = list[1].lower()

    first = word_to_pig(first)
    last = word_to_pig(last)

    x = first[0].upper()
    first = x + first[1::]

    y = last[0].upper()
    last = y + last[1::]

    latin = first + " " + last
    # latin = word_to_pig(first) + word_to_pig(last)
    return latin

word = input("Enter a word: ")
print(word_to_pig(word))
name = input("Enter your name: ")
print(name_to_pig(name))
