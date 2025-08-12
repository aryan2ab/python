class Employee:
    a = 1


class Programmer(Employee):
    b = 2

class Manager(Employee):
    c = 3


o = Employee()
print(o.a)    
#print(o.b)

o = Programmer()
print(o.a)
print(o.b)

o = Manager()
print(o.a)
print(o.c) 