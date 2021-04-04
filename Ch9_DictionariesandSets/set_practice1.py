def f1(s1, s2, op):
    if op == 1:
        temp = s1.intersection(s2)
    elif op == 2:
        temp = s1.difference(s2)
    else:
        temp = s1.union(s2)
    return temp

set1 = {'a', 'b', 'c'}
set2 = {'c', 'd'}
print(f1(set1, set2, 1))
print(f1(set1, set2, 2))
print(f1(set1, set2, 3))

set1 = {'a', 'b'}
set2 = {'c', 'd'}
print(f1(set1, set2, 1))
print(f1(set1, set2, 2))
print(f1(set1, set2, 3))
