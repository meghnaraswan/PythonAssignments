#question 1
my_list = []
for i in range(0,6,2):
    for k in range(4):
        my_list.append(i+k)

print(i)     # Line 1
print(k)     # Line 2
print(my_list)   # Line 3

#question 2
def list_ex(your_list):
    for x in range(0,6,2):
        for y in range(4):
            your_list.append(x+y)
    return your_list

print(list_ex([]))
your_list = []
print(list_ex(your_list))
your_list = [10, 20, 30]
print(list_ex(your_list))
print(list_ex(your_list))

#question 3
list_a = [1, 2, 3, 4, 5]
list_b = []

for num in list_a:
    list_b.append(num)

list_a[2] = 10
print(list_a)
print(list_b)
print(list_b[2])

#question 4
def func(number):
    total = 0
    while number > 0:
        total = total + number * (number-1)
        number -= 1
    return total

print(func(5))

#question 5
def function(x):
    total = 0
    for i in range(x):
        total += i * (i - 1)
    return total

print(function(5))

#question 6:
#Write a function that takes a string as an argument, converts the string to a list of characters, sorts the list,
#converts the list back to a string, and displays the resulting substring.
def string_sort(a_string):
    char_list = sorted(a_string)
    sorted_string = "".join(char_list)
    print(sorted_string)

#question 7:
#Write your own functions of the Python built-in functions min and max to find the minimum and maximum values within
#a list.
def min(numb_list):
    min_numb = numb_list[0]
    for numb in numb_list:
        if numb < min_numb:
            min_numb = numb
    return min_numb
def max(numb_list):
    max_numb = numb_list[0]
    for numb in numb_list:
        if numb > max_numb:
            max_numb = numb
    return max_numb

#question 8:
#Write a function that makes a list of the unique letters used in a sentence. This is, if the letter x is used twice in
#a sentence, it should appear once in your list. No punctuation should appear in your list. For the purpose of
#simplicity, consider the following characters as punctuation: .,;?!-
#Use a while loop
#Use a for loop

#for loop
def unique_letters(sentence):
    letter_list = []
    for x in sentence:
        if not(x in '.,:?!- ' or x in letter_list):
            letter_list.append(x)
    return letter_list
print(unique_letters("This is the sentence I am testing. Hey!"))
#to remove uppercase duplicates, check x.lower() in letter_list

#while loop
def unique_letters_while(sentence):
    letter_list = []
    i = 0
    while i < len(sentence):
        if not(sentence[i] in '.,:?!- ' or sentence[i] in letter_list):
            letter_list.append(sentence[i])
        i += 1
    return letter_list
print(unique_letters_while("This is the sentence I am testing. Hey!"))
#to remove uppercase duplicates, check x.lower() in letter_list

#question 9
#Write	a	Python	function	that	accepts	a	string	and	calculate	the	number	of	upper	case
#letters	and	lower	case	letters.
def upper_lower(a_string):
    up = 0
    low = 0
    for char in a_string:
        if char.isalpha():
            if char.upper() == char:
                up += 1
            elif char.lower() == char:
                low += 1
    return up, low

#question 10
#Write a function that takes a tuple as an argument and returns the tuple sorted.
def sort_tuple(a_tuple):
    sorted_list = sorted(a_tuple)
    return tuple(sorted_list)

#question 11
#. Write a function that takes a string as an argument and returns a list of the words in the string.
def words_in_string(a_string):
    return a_string.split()
