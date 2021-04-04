#factorial recursion

import math

def fact(num):
    '''calculate factorial'''
    if num == 1:
        return num
    else:
        num *= fact(num - 1)
        return num

print(math.factorial(5))
print(fact(5))
