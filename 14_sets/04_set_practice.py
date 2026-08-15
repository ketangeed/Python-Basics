a = {1, 3, 4, 66, 2, 1, 22}
print(a)

a.add(77)
print(a)

a.remove(77)
print(a)



n = int(input("Enter the value : "))
s = {1, 3, 4, 5, 6, 7, 99, 23, 3, 11, 222, 33}
for i in s:
    if i == n:
        print("Value Exist.")
    

s1 = {1, 2, 3, 44, 56, 23, 67, 12}
s2 = {1, 2, 4, 6, 7, 33, 21, 12}
s3 = s1.intersection(s2)
print(s3)