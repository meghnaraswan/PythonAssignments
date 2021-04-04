#default parameters

def calculate_sum(num1, num2, num3 = 0):
    return num1 + num2 + num3

def calcuate_avg(num1, num2, num3 = 0):
    if num3 != 0:
        return calculate_sum(num1, num2, num3)/3
    else:
        return calculate_sum(num1, num2)/2

def formatted_output(my_str, my_int):
    print("the result of the processing for", my_str, "was", my_int)

print(calculate_sum(1, 2, 3))
print(calculate_sum(2, 4))
print(calcuate_avg(1, 2, 3))
print(calcuate_avg(2, 4))

formatted_output("Bill", 100)

result = formatted_output(my_int = 75, my_str = "Fred")
print(result)
