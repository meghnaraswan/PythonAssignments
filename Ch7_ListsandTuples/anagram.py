#anagrams

#see if 2 words are anagrams

#define function for anagrams

def anagram(word1, word2):
    '''Return True if input words are anagrams, false otherwise'''
    word1_sort = sorted(word1.lower())
    word2_sort = sorted(word2.lower())

    if word1_sort == word2_sort:
        return True
    else:
        return False

#user input

word_list = input("Enter 2 words separated by a space: ").split()

is_anagram = anagram(word_list[0], word_list[1])

#report anagram to user
#check if anagram
if is_anagram == True:
    print("The words are anagrams!")
else:
    print("The words are not anagrams.")
