# write a program that counts the vowels in statement.

sentence = "I love Python Proggraming so much."

sum = 0

vowels = ["a", "e", "i","o","u"]


for char in sentence:
    if (char in vowels):
        sum += 1
print(f"The the vowels in the sentence is {sum}.")



# take a user input str and check if it is palindrome or not.

str1 = (input("enter the value : "))

if (str1 == str1[::-1]):
    print("The str1 is palindrome")
else:
    print("The str1 is not palindrome.")
    

print(str1[::-1])# advance slicing for the backword order.





i = 3

while i <= 30:
    if (i % 3 == 0):
        print(i)
    i += 1