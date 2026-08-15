s = {1, 3, 55, 3, 677, 22, 45}

s.add(67)
# s.remove(3333) # this will throw error cause the value is not present, so use discard means if the value is there remove it and if the value is not there dont throw an error.
s.discard(3333)
s.pop() #removes the random variable from set.
print(s)
