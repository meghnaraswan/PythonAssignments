number = int(input("Enter a positive number: "))

if number <= 0:
    number = int(input("Enter a positive number: "))

n = 1
step = 1
while number >= n:
    if n % 2 == 1:
        print(n, "Odd")
    else:
        print(n, "Even")
    n += step
