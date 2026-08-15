text = "I am stronger, i am smarter i am better. "
vowels = "aeiou"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(count)




# Q2 — Pattern
# Print:
# 1
# 12
# 123
# 1234

num = int(input())

for i in range(1, num+1):
    for j in range(1, i+1):
        print(j, end ="")
     
    print()


num = int(input())

for i in range(1, num+1):
    for j in range(i):
        print(i, end ="")
     
    print()







text = "I am stronger, i am smarter i am better. "
vowels = "aeiou"

for char in text.lower():
    if char in vowels:
      print(char, end=" ")

# text = "I am stronger, i am smarter i am better."
# vowels = "aeiou"

# for char in text.lower():
#     if char in vowels:
#         print(char, end=" ")



