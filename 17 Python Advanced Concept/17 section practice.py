# # Q.1

# def logger(func):
#     def wrapper ():
#         print("Function is been called")
#         func()
#     return wrapper ()

# @logger
# def hello():
#     print("Hii Ketan")


# # Q.2
# from time import time
# def timer(func):
#     def wrapper(n):
#         t1 = time()
#         func(n)
#         t2 = time()
#         print(t2 - t1)
#     return wrapper

# @timer
# def sum_s1(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum += i
#     return sum

# s = sum_s1(969)
# print(s)



# Q.3

# class Employee:
#     def __init__(self, salary):
#         self.__salary = salary

#     @property
#     def salary(self):
#         return self.__salary
#     @salary.setter
#     def salary(self, new_sal):
#         if new_sal > 0:
#             self.__salary = new_sal
#         else:
#             print("Negative Int Warning ...")

# e = Employee(50000)
# print(e.salary)
# e.salary = -4793




# # Q.4

# class Utils:
#     def __init__(self):
#         pass
  

#     @staticmethod
#     def sum1(a, b):
#         return a + b
#     @classmethod
#     def description (cls):
#         print("This is Ketan Geed..")

# s = Utils()
# print(s.sum1(3, 6))
# s.description()

# print(Utils.sum1(43, 8))
# Utils.description()

        

# Q.5
# class Book:
#     def __init__(self, title, auther):
#         self.title = title
#         self.auther = auther

#     def __str__(self):
#         return f"{self.title} by {self.auther}"

    
#     def __len__(self):
#         return len(self.title)
    
# b1 = Book("tare", "Ketan")
# print(b1)
# print(len(b1))




# Q.6
# class NegativeNumberError(Exception):
#     pass

# try :

#     a = int(input("Enter the First number : "))
#     b = int(input("Entert the second number : "))

#     print(a // b)

#     if (a < 0) or (b < 0):
#         raise NegativeNumberError ("Cannot divide by negative number")

# except ValueError :
#     print("Do not typecast wrong..")

# except ZeroDivisionError :
#     print("Do not divide by zero..")



# Q.7
# from functools import reduce

# l = [1, 2, 3, 4, 5, 6]

# def cube(x):
#     return x * (x*x)

# def even(a):
#     return a % 2 == 0

# def red(r, b):
#     return r + b
# print(list(map(cube, l)))
# print(list(filter(even, l)))

# new = reduce(red , l)
# print(new)



# Q.8


while (text := input("enter ")) != "quit":
    print(f"you entered {text}")