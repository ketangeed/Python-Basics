# # Q.1) create the class car with the method drive that prints "the car is moving". create an object of a car and call car.

# class Car:
#     def drive(self):
#         print("The car is moving")
    
# c = Car()
# c.drive()





# # Q.2) create the class Person and that accepts the name and age and stores the value and prints it.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(self.name)
#         print(self.age)
#         print(f"the name is {self.name}, and the age is {self.age}.")

# p = Person("Ketan", 20)
# p.display()




# # Q.3) create the animal sound inheritence that prints the some sound and then creates the class dog that overides the sound and create the object of the dog and call sound().


# class Animal:
#     def sound(self):
#         print("Woofff")

# class Dog:
#     def sound(self):
#         print("Bark!!!")

# a = Animal()
# a.sound()

# b = Dog()
# b.sound()
    




class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")
    

a = Dog()
a.sound()
