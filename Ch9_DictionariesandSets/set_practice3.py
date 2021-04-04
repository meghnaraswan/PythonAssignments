#first and last name common letters

#a) use lists to return a list of commn letters

def common_letter_list(first,last):
    '''takes in first and last name string, returns list of common letters'''
    common_list = []
    for f in first.lower():
        for l in last.lower():
            if (f == l) and (f not in common_list):
                common_list.append(f)
    return common_list

#b) use sets to return a set that is the intersection of both names

def common_letter_set(first, last):
    '''takes in a first and last name string, returns set of common letters'''
    return set(first.lower()) & set(last.lower())

#c) uses sets to return set that is the symmetric difference
def uncommon_letter_set(first, last):
    '''takes in a first and last name string, returns set of unique letters'''
    return set(first.lower()) ^ set(last.lower())

f_name = "Meghna"
l_name = "Raswan"
print(common_letter_list(f_name, l_name))
print(common_letter_set(f_name, l_name))
print(uncommon_letter_set(f_name, l_name))
