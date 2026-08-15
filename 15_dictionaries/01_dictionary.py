marks = {"ketan" : 99, "tony": 98, "lily" : 45}

print(marks, type(marks))

# can have any datatype
# key should be hashable, str, tuples, int but list is not hashable so we cannot have list as a keys.

print(marks["lily"]) # can check
marks["ketan"] = 100 # use to replace/check
print(marks)