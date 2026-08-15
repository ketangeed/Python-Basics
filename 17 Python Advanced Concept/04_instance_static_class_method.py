# static method dosen't use the instance method.

class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def greet(self):
        return f"the name is {self.name}, and the salary is {self.salary}."
    # Static Method
    @staticmethod
    def sum(a, b):
        return a+b
    

    # Class Method(decorator)
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def print_new_company(cls, new_com):
        cls.company = new_com
        print(new_com)

  

e1 = Employee("ketan", 56666)
# print(e1.greet())
# print(e1.sum(4, 50))
# e1.print_company()
e1.print_new_company("asus")
print(Employee.company)



 
class Gym:
    total_numbers = 0
    def __init__(self, new_member):
        self._new_member = new_member
        Gym.total_numbers += 1

    @classmethod
    def gym_info(cls):
        return f"Welcome to Power Gym! Total members: {cls.total_numbers}"
    
    @staticmethod
    def chech_bmi(weight, height):
        return weight / (height*2)
    
g = Gym("ketan")
print(g.gym_info())

print(g.chech_bmi(60, 1.8))




class Mobile:
    discount = 10

    def __init__(self, new_cos):
        self._new_cos = new_cos

    @classmethod
    def change_discount(cls, new_val):
        cls.discount = new_val
        return f"the new discount is : {cls.discount}"
     
        
    @staticmethod
    def is_valid_price(price):
        if price > 0:
            return True
        else:
            return False
        
m = Mobile("realmee")
print(m.change_discount(50))
print(m.is_valid_price(5000))
print(m.is_valid_price(-2000))