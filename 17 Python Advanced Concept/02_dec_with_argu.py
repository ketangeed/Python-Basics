# decorators are the functions that extends a function without modifying it.
def decorators(func):
    def wrapper():
        print("This is your ice cream.")
        func()
    return wrapper 

@decorators
def get_ice_cream():
    print("...here is your ice cream...")

get_ice_cream()





