text = " i love python programming "

# qs.1 remove the extra spaces from both end.
print(text.strip())


# qs.2 convert it to the title case.
print(text.title())

# qs.3 count how many times "o" appears
print(text.count("o"))


# check if the sting "123abc" is alphanumeric
txt = "123abc"

if txt.isalnum:
    print("this is alnum string")
else:
    print("this is not the alnum string")