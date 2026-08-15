# list is ordered, mutable (changeble) collection of the items.
# it is the collection of the items, and can store multiple datatypes.
# like int, str, float
# strings are imutable. but lists are.

marks = [88, 34, 56, 78, 45]
mixed = ["helo", 3.14, 78, False]

print(marks)
print(mixed)

# to access string give the idx number.
print(marks[0])
# it starts from 0.
print(mixed[2])

print(mixed[1:])

print(mixed[3]) #out of bound.