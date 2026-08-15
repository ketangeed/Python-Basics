class Employee:
    company = "Asus" #this is class attriute
    def __init__(self, salary, name, bond, company):
        self.salary = salary #create an instance attribute of name salary and assign it with salary.
        self.name = name
        self.bond = bond
        self.company = company
    def get_salary(self):
        return self.salary
    
    def info_employee(self):
        print(f"The name id {self.name}. the salary is {self.salary}, and the bond is of {self.bond} years.")

s1 = Employee(5000, "Ketan", 5, "Tesla")
print(s1.company) #this will print the instance attribute whenever present.
print(Employee.company) #this always print the class attribute.


# Object Introspection
print(dir(s1))