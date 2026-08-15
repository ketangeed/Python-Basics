# 1. The Greeting Wrapper:
# Write a decorator called hello_decorator that prints "Before the function" before calling the original function, and "After the function" after it.

# def hello_decorator(func):
#     def wrapper():
#         print("Before the function.")
#         func()
#         print("After the function.")
#     return wrapper
# @ hello_decorator
# def greet():
#     print("Hello!!!")
# greet()

# 2. The Double Maker:
# Write a decorator that takes a function returning a number and doubles that number before returning it to the user.

# def double_decorator(func):
#     def wrapper():
#         result = func() * 2
#         return result
#     return wrapper

# @double_decorator
# def given_number():
#     return 5

#     # return 5

# print(given_number())


# 3. The Authorization Gate:
# Imagine a variable is_admin = False. Write a decorator that only allows a function to run if is_admin is True. If not, it should print "Access Denied."

is_admin = True
def admin_only(func):
    def wrapper():
        if is_admin == True:
            func()
        else:
            print("Access Denied! You are not an admin.")
    return wrapper

@admin_only
def secret_data():
    print("the secret AI formula is 42.")

secret_data()


# 4. The Timer (Advanced):
# Write a decorator that prints "Starting timer..." then runs the function, then prints "Time finished!"


# def timer_decorator(func):
#     def wrapper():
#         print("Timer started.")
#         func()
#         print("timer finished!")
#     return wrapper
# @ timer_decorator
# def run_race():
#     print("The runners are sprinting..")
# run_race()



# 5. The Upper-Case Transformer:
# Write a decorator that takes a function returning a string (like "hello") and converts that string to all caps ("HELLO").

# def make_upper(func):
#     def wrapper ():
#         result = func().upper()
#         return result
#     return wrapper

# @ make_upper
# def get_message():
#     return "i am becoming python pro, i am coding god."

# print(get_message())