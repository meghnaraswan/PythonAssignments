#Write a function that takes in a string and a list of words as parameters and returns True if the word exists in the
#list more than one and False otherwise.

def is_multiple_words(test_string, word_list):
    occurences = word_list.count(test_string)
    if occurences > 1:
        return True
    else:
        return False

list_a = ['hat', 'the', 'bad', 'appreciate', 'good', 'illicit', 'hat', 'dark', 'science']

print(is_multiple_words('hat', list_a))
print(is_multiple_words('good', list_a))
print(is_multiple_words('computer', list_a))


#Write a function that takes a list of integers as inout and returns True if the sum of integers in the list is a
#perfct square and False otherwise

def is_perfect_square(int_list):
    import math
    total = sum(int_list)
    root = math.sqrt(total)
    if int(root) == root:
        return True
    else:
        return False

print()
print(is_perfect_square(([1, 2, 3, 3])))
print(is_perfect_square([4, 5, 6, 7]))


#Write a function that takes a list of strings as input and alters the list so it only contains strings that start with
#vowels. The method should return a list of all strings removed from the original list.

def vowel_words(word_list):
    word_tuple = tuple(word_list)
    consonant_words = []
    for word in word_tuple:
        if not(word[0].lower() in 'aeiou'):
            index = word_list.index(word)
            consonant_words.append(word_list.pop(index))

    return consonant_words

print()
print(vowel_words(list_a))
print(list_a)



