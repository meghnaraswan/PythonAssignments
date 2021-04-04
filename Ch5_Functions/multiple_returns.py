#multiple returns
def positive_negative_zero(number):
    '''tell me positive,negative, or zero'''
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"

def positive_negative_zero2(number):
    #another approach
    if number > 0:
        answer = "positive"
    elif number < 0:
        answer = "negative"
    else:
        answer = "zero"
    return answer

print(positive_negative_zero(0))
print(positive_negative_zero(7))
print(positive_negative_zero(-3))
print(positive_negative_zero2(0))
print(positive_negative_zero2(7))
print(positive_negative_zero2(-3))
