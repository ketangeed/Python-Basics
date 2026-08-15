marks = [6, 3, 9, 2, 6]
print(marks)
print(max(marks)) # its short form to find the largest value from list.


marks.append(9)
print(marks)

marks.pop() # will remove the last element from the list.
marks.pop(1) # will pop out the idx number element.
print(marks)

marks.insert(2, 55) #will insert 55 at 2 idx.
print(marks)


a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 0]
a.extend(b)
print(a) # will add the list in another list.
a.remove(0) # removes the element.
print(a)

b.reverse() # will reverse the list
print(b)

a.count(1)
print(a)