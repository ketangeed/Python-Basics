set1 = {1, 2, 3, 3, 4, 6}
print(set1)

set1.add(5)
set1.remove(2)
print(set1)


a = {1, 2, 3}
b = {3, 4, 5}

c = a.union(b)
print(c)

d = a.intersection(b)
print(d)

e = a.difference(b)
print(e)