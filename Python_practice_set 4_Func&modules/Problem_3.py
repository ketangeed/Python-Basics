#qs.1 write the lambda funtion that adds the two numbers and test it.


sum = lambda x, y : x + y

print(sum(3, 7))



# qs.2 create the list [1,2,3,4,5] use map() with lambda function to get there squares.

list1 = [ 1, 2, 3, 4, 5]
square = lambda x : x*x

print(list(map(square, list1)))



# Neural Mamba pattern babyyy
for int in list1:
    if (int != 0):
        print(int*int, end=" ")
    else:
        print()
    
  

