class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        return f"the name is {self.name}, and the salary is {self.salary}."
    
    def __str__(self):
        return f"the name is {self.name}, and the salary is {self.salary}."
    
    def __repr__(self):
        return f"name : {self.name}, salary : {self.salary}."
    

e = Employee("ketan", 345678)

print(e.show())
print(str(e))
print(repr(e))