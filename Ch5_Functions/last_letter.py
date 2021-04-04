#Write a function, last_letter, that takes a string as a parameter and returns the last character in the string.

word = input("Enter a word that you want to find the last character of: ")

def last_letter(word):
    return word[-1]

print("The last character of", word, "is", last_letter(word))
