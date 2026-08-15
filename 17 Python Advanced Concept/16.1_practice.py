# getter and setter.


class Whether:
    def __init__(self, temp):
        self._temp = temp

    @property
    def temp(self):
        return f"{self._temp}"
    
    @temp.setter
    def temp(self, new_temp):
        if new_temp < -100:
            print("That's too much temp.")
        else:
            self._temp = new_temp


temperature = Whether(-50)
print(temperature.temp)
temperature.temp = -199
print(temperature.temp)



class Person:
    def __init__(self, age):
        self._age = age


    @property
    def age(self):
        return f"Age is : {self._age}"
    
    @age.setter
    def age(self, new_age):
        if new_age > 0 and new_age < 120:
            self._age = new_age
        else:
            print("are you human or not?...")
        
a = Person(50)
print(a.age)
a.age = 5555
print(a.age)




class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return f"{self._price}"
    
    @price.setter
    def price(self, new_price):
        if new_price < 0:
            self._price = 0
            print("Price cannot be in negative.. setting it as 0.")
        else:
            self._price = new_price

p = Product(55)
print(p.price)
p.price = 555
print(p.price)
p.price = -5000
print(p.price)




class Contact:
    def __init__(self, phone):
        self._phone = phone

    @property
    def phone(self):
        return f"{self._phone}"
    
    @phone.setter 
    def phone(self, new_phone):
        if len(str(new_phone)) == 10:
            self._phone = new_phone
        else:
            print("Invalid phone")

num = Contact(123334567809)
print(num.phone)
num.phone = 1246689865
print(num.phone)


# class and static method

class Student:
    total_students = 0
    def __init__(self, new_student):
        self._new_student = new_student
        Student.total_students += 1
        

    @classmethod
    def show_total(cls):
        return f"total students are : {cls.total_students}"
    
    @staticmethod
    def is_holiday(day):
        if day == "Sunday":
            return True
        else:
            return False

s1 = Student("Ketan")
s2 = Student("Rahul")

print(s1.total_students)
print(s1.show_total())
print(s2.is_holiday("Sunday"))




class Book:

    def __init__(self, title, pages):
        self._title = title
        self._pages = pages

    
    def __str__(self):
        return f"the title of the book is : {self._title}."
    
    def __len__(self):
        return self._pages
    

b1 = Book("surrounded by idiots", 999)
print(len(b1))
print(b1._title)



class Vehicle:
    def __init__(self, brand):
        self._brand = brand
    def drive(self):
        return f"Driving {self._brand}"

class Car(Vehicle):
    def honk(self):
        return "Beep Beep!"
   
c1 = Car("Tesla")
print(c1.honk())
print(c1.drive())




class Mobile:
    discount = 10
    def __init__(self, val):
        self._val = val

    @classmethod
    def new_val(cls, new_val):
        cls.discount = new_val


    @staticmethod
    def is_valid_price(price):
        if price > 0:
            return True
        else:
            return False

m = Mobile("iphone")
print(m.discount)
m.new_val(50)
print(m.discount)


