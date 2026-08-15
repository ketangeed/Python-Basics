a = [1, 2, 3, 4, 5]
print(a)


b = [2, 3, 42, 51, 66, 8, 40, 26 ]
for i in b:
    if i % 2 == 0:
        print(i)

print(sum(b))
print(max(b))

c = [3, 22, 44, 4, 6, 78, 5, 99]
count = 0
for i in c:
    if i > 10:
        count += 1
print(count)

