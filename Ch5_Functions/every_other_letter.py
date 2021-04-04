#Write a function, everyother, that takes a string as a parameter and returns a string of every other character from the string.

word = input("Enter a word that you would like to find every other letter of: ")

def everyother(word):
    return word[::2]

print("Every other letter for the word", word, "is", everyother(word))
