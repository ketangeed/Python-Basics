# __init__ = a special function that runs automatically when you create an object.




class Employee:
    def __init__(self, salary, name, bond):
        self.salary = salary #create an instance attribute of name salary and assign it with salary.
        self.name = name
        self.bond = bond
    def get_salary(self):
        return self.salary
    
    def info_employee(self):
        print(f"The name id {self.name}. the salary is {self.salary}, and the bond is of {self.bond} years.")


e1 = Employee(500000, 'Ketan', 5)
print(e1.get_salary())

print(e1.info_employee())



class Student:
    def __init__(self, name):
        self.name = name

s = Student("Ketan")
print(s.name)


class Car:
    def __init__(self, name):
        self.name = name
    
    def car_info(self):
        return f"The car is {self.name}"
        
s1 = Car("BMW")
print(s1.car_info())



class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}"
p = Person("Ketan")
print(p.greet())








