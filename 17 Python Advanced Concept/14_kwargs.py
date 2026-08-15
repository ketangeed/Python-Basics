def marks(**kwargs):
# kwargs is a dictionary with all the key value pairs which were passed to marks..
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")
    
marks(ketan=45, shubham=9, uiwr=89, hwebf=13)
