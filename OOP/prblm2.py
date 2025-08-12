class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
            print(f"Square of {self.n} is {self.n * self.n}")
    
    def cube(self):
            print(f"Cube of {self.n} is {self.n * self.n * self.n}")

    def squareroot(self):
            print(f"Squareroot of {self.n} is {self.n * 0.5}")        
a = Calculator(4)
a.square()  
a.cube()
a.squareroot()
# Outputs: Square of 5 is 25            