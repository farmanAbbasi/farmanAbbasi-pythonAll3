#example working in python3 python2 style
from functools import cmp_to_key

a = [[2, 3], [3, -1], [1, 1]]

def compare(a, b):
    if a[0] < b[0]:
        return -1
    elif a[0] > b[0]:
        return 1
    else:
        return 0

sorted_a = sorted(a, key=cmp_to_key(compare))
print(sorted_a)

#python2
a = [[2, 3], [3, -1], [1, 1]]

def compare(a, b):
    if a[0] < b[0]:
        return -1
    elif a[0] > b[0]:
        return 1
    else:
        return 0

sorted_a = sorted(a, cmp=compare)
print(sorted_a)



#python3
a = [[2, 3], [3, -1], [1, 1]]

def compare(item):
    return item[0]

sorted_a = sorted(a, key=compare)
print(sorted_a)
