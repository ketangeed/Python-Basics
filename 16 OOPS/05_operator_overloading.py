class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self, p):
        return Points(self.x + p.x, self.y + p.y)
    
    def show(self):
        print (f"The x is {self.x} and the y is {self.y}")
    
    def __add__(self, p):
        return Points(self.x + p.x, self.y + p.y)
    
    def __mul__(self, p):
        return Points(self.x * p.x, self.y * p.y)




s1 = Points(3, 6)
s2 = Points(5, 9)

# print(s1.sum(s2)) #so can we instead do this s1 + s2, no we cant we have to overide the operator.
# now 
s = s1*s2
s.show() 

# "+" = __add__
# "-" = __sub__
# "*" = __mul__
# "/" = __truediv__