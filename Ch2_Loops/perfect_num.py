#
top_num = int(input("What is the upper number for the range: "))

number = 2
while number <= top_num:
    #sum divisors
    divisor = 1
    sum_of_divisors = 0
    while divisor < number:
        if number % divisor == 0:
            sum_of_divisors = sum_of_divisors + divisor #sum_of_divisors += divisor
        divisor += 1

    #classify the number based on its divisor sum
    if number == sum_of_divisors:
        print(number, "is perfect")
    elif number < sum_of_divisors:
        print(number, "is abundant")
    elif number > sum_of_divisors:
        print(number, "is deficient")
    number += 1
