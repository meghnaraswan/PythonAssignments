#mutable parameters

def list_change(list_input):
    list_param = list_input[:]
    list_param.sort()
    list_param.append('the end')
    return list_param

list_a = [1, 5, 7, 3, 8, 9, 6, 4, 3, 5, 4]

list_b = list_change(list_a)

print(list_b)
print(list_a)
