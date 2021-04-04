#functions practice exercises - solutions

def reverse(stringy):
    return stringy[::-1]

def last_letter(stringy):
    return stringy[-1]

def everyother(stringy):
    return stringy[::2]

def is_vowel(character):
    vowels = 'aeiou'
    return character.lower() in vowels

def vowel_count(stringy):
    count = 0
    for x in stringy:
        if is_vowel(x):
            count += 1
    return count

def calculate_sum(num1,num2):
    return num1 + num2

def calculate_avg(num1,num2):
    return calculate_sum(num1, num2)/2

def max(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    elif num3 >= num1 and num3 >= num2:
        return num3

def consecutive(num1,num2):
    return num1 == num2 + 1 or num2 == num1 + 1


print(reverse('Chapman'))
print(last_letter('Chapman'))
print(everyother('Chapman'))
print(is_vowel('e'))
print(is_vowel('x'))
print(vowel_count("This is a sentence."))
print(calculate_sum(3, 7))
print(calculate_avg(3, 7))
print(max(3, 9, 6))
print(max(9, 9, 3))
print(consecutive(3, 4))
print(consecutive(4, 3))
print(consecutive(2, 8))
print(consecutive(8, 2))

