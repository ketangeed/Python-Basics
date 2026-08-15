info = {"name": "Ketan", "age": 20, "city": "shirpur"}
print(info)


info["college"] = "RCPCOEP"
print(info)
info["age"] = 19
print(info)

print(info.keys())

count = 0
for i in info:
    
    if type(i) ==  type(int):
        count += 1
print(count)
