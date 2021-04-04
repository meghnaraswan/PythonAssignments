#Write a function, reverse, that takes a string as a parameter and returns the string in reversed order.

word = input("Enter a word that you want to reverse: ")

def reverse(word):
    return word[::-1]

print("The reverse of", word, "is" ,reverse(word))


