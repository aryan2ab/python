class Employee:
    company = "TechCorp"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


#class Programmer:
 #   company = "MicroTech"
  #  def show(self):
   #     print(f"The name is {self.name} and the salary is {self.salary}")   
#
 #   def show_language(self):
  #      print(f"The programming language is {self.language}")   
class Programmer(Employee):
    company = "ITC"
    def show_language(self):
        print(f"the name is {self.name} and the language is {self.language}")


a = Employee()
b = Programmer()

print(a.company, b.company)