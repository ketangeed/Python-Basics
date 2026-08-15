template = "hi {}, you have {} in your bank"

a = "ketan"
a1 = 1000

b = "krishna"
b1 = 2000

s1 = template.format(a, a1)
print(s1)

#  can use like this

print(f"hi {a}, and  {b}, you both have {a1} and {b1}, in your bank account. and your sum is : ", a1 + b1)