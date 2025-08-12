class Employee:
    
    language = "Python"
    salary = 1200000

    def getInfo(self):
        print(f"Language: {self.language}, Salary: {self.salary}")


aryan = Employee()
#aryan.language = "JavaScript"  # Overriding class attribute for this instance
#print(aryan.language, aryan.salary) 

aryan.getInfo()  # Outputs: Language: JavaScript, Salary: 1200000