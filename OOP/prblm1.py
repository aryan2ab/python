class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

p = Programmer("Aryan", 1200000, 751024)
print(p.name, p.salary, p.pincode)
r = Programmer("Rohan", 1300000, 751025)
print(r.name, r.salary, r.pincode)
