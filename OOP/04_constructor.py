class Employee:
    
    language = "Python"
    salary = 1200000

    def __init__(self, name, salary, language): #dunder method which is automatically called when an object is created
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"Language: {self.language}, Salary: {self.salary}")

        @staticmethod
        def greet():
            print("Hello from Employee class!")


aryan = Employee("Aryan", 1300000, "JavaScript")  # Creating an instance of Employee
#aryan.name = "Aryan"
print(aryan.name, aryan.language, aryan.salary)  # Outputs: Ary

#aryan.language = "JavaScript"  # Overriding class attribute for this instance
#print(aryan.language, aryan.salary) 
#aryan.greet()
#aryan.getInfo()
  # Outputs: Hello from Employee class!