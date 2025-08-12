class Employee:
    
    language = "Python"
    salary = 1200000


aryan = Employee()
aryan.name = "Aryan"
print(aryan.name, aryan.language, aryan.salary)      

#Here name is object attribute, while language and salary are class attributes.
#Object attributes are specific to the instance, while class attributes are shared across all instances of the class.