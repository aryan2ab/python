class Employee:
    company = "TechCorp"
    name = "default_name"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def print_language(self):
        print(f"The programming language is {self.language}")
#class Programmer:
 #   company = "MicroTech"
  #  def show(self):
   #     print(f"The name is {self.name} and the salary is {self.salary}")   
 #   def show_language(self):
  #      print(f"The programming language is {self.language}")   
class Programmer(Employee, Coder):
    company = "ITC"
    def show_language(self):
        print(f"the name is {self.company} and the language is {self.language}")


a = Employee()
b = Programmer()

b.show()
b.print_language()
b.show_language()
print(a.company, b.company)