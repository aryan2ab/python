class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
            print(f"Square of {self.n} is {self.n * self.n}")
    
    def cube(self):
            print(f"Cube of {self.n} is {self.n * self.n * self.n}")

    def squareroot(self):
            print(f"Squareroot of {self.n} is {self.n * 0.5}")   

    @staticmethod
    def hello():
          print("Hello from Calculator class!")             
a = Calculator(4)
a.hello()  # Outputs: Hello from Calculator class!
a.square()  
a.cube()
a.squareroot()