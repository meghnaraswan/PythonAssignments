#palindromes

import string

#get user input
original_str = input("Input a string: ")

#process string for plaindrome check
#make string lowercase
modified_str = original_str.lower()

#remove punctuation and whitespace
bad_chars = string.punctuation + string.whitespace

for char in bad_chars: #iterate over bad character string
    modified_str = modified_str.replace(char, "")

#plaindrome visualization
print("Original string: "+original_str)
print("Modified string: "+modified_str)
print("Reversed string: "+modified_str[::-1])

#check forward and reverse
if modified_str == modified_str[::-1]:
    print("Palindrome!")
else:
    print("Fail! You do not have a palindrome.")
