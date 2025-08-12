def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1,34,23456,45,345678,34567,1234567890,45,765,0,98765]

f = list(filter(divisible5, a))
print(f)
