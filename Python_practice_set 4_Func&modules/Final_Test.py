name = "Ketan"
rev = ""
for char in name:
    rev =  char + rev
print(rev)


text = "i love python progrming language."
vowels = ['a','e','i','o','u']
count_vowels = 0
count_cosonants = 0
for ch in text.lower():
    if ch in vowels:
        count_vowels += 1
    else:
        count_cosonants += 1
    
print(count_vowels)
print(count_cosonants)


l = [1, 33 , 44, 45, 23, 90, 98, 67, 82]

for i in l:
    if i>50:
        print(i, end=" ")

name = "madam"
rev = ""
rev = ""
def pali(name):
    for char in name:
        global rev
        rev = char + rev
    if name == rev:
        print("Palindrome")
    else:
        print("Not palindrome")  
               
pali("madam")



num = int(input("Enter the number : "))
for i in range(1, num+1):
    for j in range(1, i+1):
        print(j, end="")
    print()




 