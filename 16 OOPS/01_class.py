# Class is blueprint or template. E.g form for an exam that contains name, age, electives, fathers name etc...

# Object: specific instace created from a templete (class). E.g form that contains he data of john doe.
# Real world entity considered as an object.
# object = data + methods
# data = information of that object.
# Methods = functions of that object.
# Classes are the group of this entities.(Blueprint/template)


# class Employee:
#     company = "HP"


#     def get_salary (self): # self is the object of the class which is being created. 
# # for like every object is created is self.
#         return 50000
    
# s1 = Employee() #An object of the class Employee id created here.
# print(s1.get_salary()) #employee s1's salary method is called.

# s2 = Employee()
# print(s2.company)


# class   Cat:
#     name = "Tom"

# s = Cat()
# print(s.name)


# gate smashers :
class Faculty:
    def put_data (self):
        self.name = input("Enter your name : ")
        self.age = int(input("Enter your age: "))
        self.salary = float(input("Enter your salary : "))

    def display(self):
        print("The name of the faculty member is :",self.name)
        print("The age is : ", self.age)
        print("The salary of the faculty member is : ", self.salary)

s = Faculty()
s.put_data()
s.display()
