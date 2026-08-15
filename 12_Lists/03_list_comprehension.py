# create the list countaning the 5 table.

a = 5     
table = []
for i in range(1, 11):
    table.append(5*i)
print(table)

'''this is the long method goof for readbility, 
bt there list comprehension to the task.'''

table = [5 * i for i in range(1, 11)]
print(table)

square = [x*x for x in range(5)]
print(square)