class Employee:
    
    language = "Python"
    salary = 1200000

aryan = Employee()
aryan.language = "JavaScript"  # Overriding class attribute for this instance
print(aryan.language, aryan.salary)  # Outputs: JavaScript 1200000