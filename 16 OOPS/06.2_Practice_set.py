# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def deposite(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#         else:
#             print("Insufficient balance.")

#     def show(self):
#         return f"Name : {self.name}, Balance : {self.balance}"
# acc = BankAccount("Ketan", 5000)
# acc.withdraw(500)
# print(acc.show())


# class Vehicle:
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed

#     def show(self):
#         return f"Brand : {self.brand}, Speed : {self.speed}"

# class Car(Vehicle):
#     def __int__(self, brand, speed, fuel_type):
#         super().__init__(brand, speed)
#         self.fuel_type = fuel_type

#     def show(self):
#         return f"Brand : {self.brand}, Speed : {self.speed}, Fuel_tupe : {self.fuel_type}"

# s = Car( "BMW", 120, "Petrol")
# print(s.show())


# class Vehicle:
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed

#     def show(self):
#         return f"Brand: {self.brand}, Speed: {self.speed}"


# class Car(Vehicle):
#     def __init__(self, brand, speed, fuel_type):
#         super().__init__(brand, speed)
#         self.fuel_type = fuel_type

#     def show(self):
#         return f"Brand: {self.brand}, Speed: {self.speed}, Fuel: {self.fuel_type}"


# c1 = Car("BMW", 120, "Petrol")
# print(c1.show())




class User:
    def __init__(self, name):
        self.name = name
    def login(self):
        return f"User {self.name} is logged in."

class Admin(User):
    def dlt_user(self):
        return f"Admin {self.name} deleted the user."

s = Admin("Ketan")
print(s.login())
print(s.dlt_user())