class Employee:
    salary = 50000
    increment = 1.05

    @property
    def salary_after_increment(self):
        return self.salary + self.salary * (self.increment / 100)

    @salary_after_increment.setter
    def salary_after_increment(self, new_salary):
        self.increment = ((new_salary / self.salary) - 1) * 100


e = Employee()
e.salary_after_increment = 445678
print(e.increment)  # Output: ((280.8 / 50000) - 1) * 100
