# qs.1) use a for loop to print from 1 to 10 but stop when the number is 7. using break.
for i in range(1, 11):
    print(i, end=" ")
    if i == 7:
        break



#  print the number from 1 to 10 and skip the number 5 using the continue.

for i in range(1, 11):
    if i == 5:
        continue
    print(i)



# write a loop that goes through a number 1 to 5, but does nothing.

for i in range(1, 6):
    print(i)
    if i == 5:
        pass
   

