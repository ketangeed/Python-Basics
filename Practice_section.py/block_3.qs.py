# Q1.Take a string and print:
# first character
# last character
name = "Ketan"
print(name[0])
print(name[-1])
# Q2
# Take a string and print it in reverse
name = "NeuralMamba"
print(name[::-1])
# Q3.
# Take a string and print only first 4 characters
name = 'chatgpt'
print(name[0:4])
#Q4 (IMPORTANT)
# Take a string and count how many characters it has
name = "Ketan"
print(len(name))
# Q5 (LOGIC BUILDER)
# Take a string and print:
# characters at even index
name = "KetanGeed"
print(name[0:9:2])
# or
print(name[::2])



# Q6. Take a string and convert it to UPPERCASE
text = "python"
print(text.upper())
print(text.lower())
# Q7. Take a string with spaces and remove spaces.
text = " Ketan Geed . "
print(text.strip()) # only removes the front and end spaces.
# Q8.Replace word "bad" with "good"
text = "Python is bad."
print(text.replace("bad", "good"))
# Q9.Count how many times letter "a" appears.
text = "A car is awesome"
print(text.count("a"))
# # Q10 (IMPORTANT)
# Find position of character "e" in a string
text = "elephant"
print(text.find("e"))



# Q1.Take a string and check if it is palindrome
# (e.g. madam → palindrome)
text = "level"
if text == text[::-1]:
    print("Palindrome.")
else:
    print("not palindrome.")

# Q2
# Take a string and count vowels

text = "i love python"
vowels = ["a","e","i","o","u"]
count = 0
for char in text:
    if char in vowels:
        count += 1
print(count)

# # Q3. Take a string and print:
# every second character in reverse
string = "python"
print(string[-1:-6:-2])

# Q4 (COMBO LOGIC)
# Take a number:
# if even → print square
# if odd → print cube

num = int(input("enter the number : "))
if num % 2 == 0:
    print("even", "and the square will be :",num*num)
else:
    print("odd","the cube will be : ", num**3)


# Q5 (CHALLENGE)

# Take a number n and print:

# 1
# 12
# 123
# 1234
# ...

num = int(input("enter the number : "))
for i in range(1, num+1):
    print("i" * i)