from functools import reduce
l = [1,34,23456,45,345678,34567,1234567890,45,765,0,98765]

def greater(a, b):
    if(a>b):
        return a
    return b

print(reduce(greater, l))