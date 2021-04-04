# create a dictionary or numbers to words
num_dict={'0':'zero','1':'one','2':'two','3':'three','4':'four',\
          '5':'five','6':'six','7':'seven','8':'eight','9':'nine'}

# prompt for user input
num_str=input("Enter an integer to convert to words: ")
print()
# go through numbers in user input and print value of number from dictionary
for num in num_str:
    print(num_dict[num], end=' ')


def integer_to_words(numbers):
    num_dict={'0':'zero','1':'one','2':'two','3':'three','4':'four',\
          '5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
    num_words = ''
    for i in numbers:
        num_words += num_dict[i] + ' '
    return num_words
print()

nums = input("Enter an integer to convert to words: ")
print(integer_to_words(nums))
