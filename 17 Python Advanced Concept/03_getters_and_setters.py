# You use a Getter when you want to control how someone sees the information.



class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property #by doin this the first name has become the property. and now i can access like belowww, it is used to get the property
    def first_name(self):
        l = self.name.split(" ") #this creates the list
        # print(l)
        return l[0] # and this is the idx number of the list
    

    @first_name.setter
    def first_name(self, first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name


e = Employee("Ketan Geed", 5000000)
# print(e.first_name())
# e.set_first_name("Spartan")
# print(e.name)


# instead of this can i do this :

print(e.first_name)
e.first_name = "spartan"
print(e.name)