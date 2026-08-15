def sum(a, b):
    print("i m summing...")
    c = a + b
    global z # pls modify global z.
    z = 0 # this refer to the global z and not create the local variable.
    return c

z = 2
print(sum(2, 7))
print(z)

# execssive use of global is discouged