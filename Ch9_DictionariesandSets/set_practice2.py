#return list of unique characters in string

#use sets

def unique_set(input_str):
    '''return list of unique characters in a string'''
    my_set = set(input_str.lower())
#    my_set = set()
#    for char in input_str:
#        my_set.add(char.lower())
    return my_set

def unique_list(input_str):
    '''return lsit of unique characters in a string'''
    my_list = []
    for char in input_str:
        if char not in my_list:
            my_list.append(char)
    return my_list

print(unique_set("hello, a string"))
print(unique_list("hello, a string"))
