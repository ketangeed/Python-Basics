# class = data + methods(function)
# in class we have 2 kind of things which are :
# data = (variables)
# e.g x = 5, y = 6, z = 7
# this are the variables works as a data in class.
# they are known as the property.
# and the functions that we store are called as Methods.


# after making the class we have to make an step 1 which is to make a empty object.

# Constructor is a special method within the class that gets automatically excuted once the object is created.


class School:
    def __init__(self, rollno, name, marks):
        self.rollno = rollno
        self.name = name
        self.marks  = marks
    
    def avg(self):
        return sum(self.marks)/len(self.marks)
    
s1 = School(10, 'Ketan', [20, 19, 17, 18])
print(s1.name)
print(s1.avg())