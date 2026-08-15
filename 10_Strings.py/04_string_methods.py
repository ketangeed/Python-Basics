# name = "ketan" # str are imutable

# # name[2] = "R" (you cannot do that.)

name = "KetanGeed"
a = len(name)
print(a)

print(name.upper())
print(name.lower())
print(name.capitalize()) # so it capatalize the 1st str.


# text = " Hello World "

# print(text.strip()) # result = "Hello World"
# print(text.lstrip()) # result = "Hello World "
# print(text.rstrip()) # result = " Hello World"


# # Find and Replace

# txt = "Python is Great"
# print(txt.find("is"))
# print(txt.replace("Great","Best"))



text = "Python123"
print(text.isalpha())#output false (only for alphabet)
print(text.isdigit()) #output is false
print(text.isalnum()) #output is true alpha+number
print(text.isspace()) #output is false