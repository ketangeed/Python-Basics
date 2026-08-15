# dictioonaries...
# Q1
# Create dictionary with:name,age,city
# Print all values

student = {
    "name" : "Ketan",
    "age"  : 18,
    "city" : "Shirpur"
}
print(student["name"], student["age"], student["city"])
student["college"] = "RCPCOEP"


# Q.2 add new key( college )
print(student["name"], student["age"], student["city"], student["college"])

# Q.3 update the key
student["age"] = 20
print(student["name"], student["age"], student["city"], student["college"])

# Q.4 print only keys: 
print(student.keys())

# Q5 (IMPORTANT)
# Count how many values are integers
txt = { "user " : 123, "age" : 15}
count = 0
for key in txt.values():
    if isinstance(key, int):
        count += 1
print(count)