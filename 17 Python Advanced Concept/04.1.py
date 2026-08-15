# class Car:
#     factory_location = "Tokyo!!"


#     def __init__(self, model):
#         self.model = model

#     @classmethod
#     def change_location(cls, new_location):
#         cls.factory_location = new_location


#     @staticmethod
#     def check_method(a):
#         if a > 5:
#             return True
#         else:
#             return False
        

# c1 = Car("bmw")
# c1.change_location("usa")
# print(c1.factory_location)
# print(c1.check_method(30))




def decorator (func):
    def wrapper(a):
        func()
        a * 2
    return wrapper
@decorator
def num(a):
    return a
num(5)
