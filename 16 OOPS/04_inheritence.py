class Animal: #this is a parent class(Super class)
    location = "Australia"
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Speaking now")


class Dog(Animal): # dog inherits from parents(subclass)
    def speak(self):
        print("Wooofff")


class Cat(Animal):
    def speak(self):
        print("Meowww")

my_dog = Dog("Rover")
my_cat = Cat("Juliee")


print(my_dog.name)
my_dog.speak()
print(my_cat.name)
my_cat.speak()








# Super() = inside the child class super lets you use the method from parents class, this is useful when you want to extend the parents behavior instead of completely replacing it.


class Animal: #this is a parent class(Super class)
    location = "Australia"
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Speaking now")


class Dog(Animal): # dog inherits from parents(subclass)
    def speak(self):
        super().speak()
        print("Wooofff")

d = Dog("Bruno")
d.speak()
