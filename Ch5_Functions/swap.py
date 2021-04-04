def swap(aa, bb):
    aa, bb = bb, aa
    return aa, bb

def sortme(ll):
    # ...
    return ll

if __name__ == '__main__':
    a = 2
    b = 5
    print("a:{}, b:{}".format(a,b))
    a,b = swap(a, b)
    print("a:{0}, b:{1}".format(a,b))

    lst = [4,15,7,89,10,7,3,4,90,]
    print(lst)
    # outout shoudl be lst is sorted
    lst = sortme(lst)
    print(lst)