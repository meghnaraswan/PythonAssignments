#factorial as a while loop
import math

num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial*i #factorial *= i
print("The factorial of", num, "is", factorial)

factorial = 1
x = 1
while x <= num:
    factorial *= x
    x += 1
print("The while factorial of", num, "is", factorial)

print(math.factorial(num))
