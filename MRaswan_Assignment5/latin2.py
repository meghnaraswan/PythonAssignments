#Meghna Raswan
#2337415
#raswan@chapman.edu
#CPSC 230-10 (1515)
#Assignment 5
#pig latin

#if the first character is a vowel, the function is true
def is_vowel(ch):
    if ch in "aeiou":
        return True
    else:
        return False

#this fuction id for when the word srtarts with consonant
def get_prefix_suffix(word):
    prefix = ""
    suffix = word
    suffix_index = 0 #start with first letter of the word
    for x in word:
        if not is_vowel(x):
            prefix = prefix + x #keeps track of first consonant
            suffix_index = suffix_index + 1 #keeps looping in for loop until reaches vowel
            continue
        else:
            suffix = suffix[suffix_index::] #starts at first vowel
            break
    return (prefix, suffix)

#changing word to pig latin
def word_to_pig(word):
    latin = ""
    first = word[0]
    if is_vowel(first):
        word += 'yay' #if it starts with vowel, call is_vowel fucntion and add 'yay'
    else:
        (pre, suff) = get_prefix_suffix(word) #if it starts with consonant, call get_prefix_suffix fucntion and add 'ay'
        x = suff + pre
        x += 'ay'
        word = x
    latin = word
    return latin

#changing name to pig latin
def name_to_pig(name):
    list = name.split() #words split into list by whitespace
    first = list[0].lower() #lowercase first word
    last = list[1].lower() #lowercase second word

    first = word_to_pig(first) #calling word_to_pig function to change first name to pig latin
    last = word_to_pig(last) #calling word_to_pig function to change last name to pig latin

    x = first[0].upper() #uppercase first letter after changing word to pig latin
    first = x + first[1::] #concatenating uppercase letter to rest of string

    y = last[0].upper() #uppercase last letter after changing word to pig latin
    last = y + last[1::] #concatenating uppercase letter to rest of string

    latin = first + " " + last #adding the names and whitespace
    return latin

#user inout for word
word = input("Enter a word: ")
print(word, "in pig-latin is", word_to_pig(word))
#user input for irst and last name
name = input("Enter your first and last name: ")
print(name, "in pig latin is", name_to_pig(name))
