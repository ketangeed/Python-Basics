# decorators : 
# Top Floor (The Decorator Name): def my_decorator(func):
# हे नाव आहे. हे 'func' ला (तुझ्या गिफ्टला) पकडून ठेवतं.
# Middle Floor (The Wrapper): def wrapper():
# खरा राडा इथे होतो. गिफ्ट उघडण्यापूर्वी काय करायचं आणि नंतर काय करायचं, ते इथे ठरतं.
# The Delivery (The Return): return wrapper
# शेवटी, पूर्ण पॅक केलेलं गिफ्ट परत पाठवायचं.


# 1. EASY (The Multiplier - दुप्पट करणारा)
# एक decorator बनवा ज्याचं नाव असेल double_it. तो एका function ला wrap करेल जो एखादा number return करतो. Decorator ने त्या number ला २ ने गुणून (multiply करून) return केलं पाहिजे.
# Example: जर function ने 10 दिलं, तर decorator मुळे 20 आलं पाहिजे.

def double_it(func):
    def wrapper(value):
        result = value*2
        return result
    return wrapper

@double_it
def num():
    print("the double of the number..")

print(num(10))



# 2. एक decorator बनवा ask_name. तो function run करण्याआधी print करेल: "नमस्कार! आपण आता [function_name] run करत आहोत...".
# Hint: func.__name__ वापरून तुला function चं नाव मिळेल.

def ask_name(func):
    def wrapper():
        print(f"नमस्कार! आपण आता {func.__name__} run करत आहोत...")
        return func()
    return wrapper

@ask_name
def func_name():
    print("My name function is running.")

func_name()




# 3. MEDIUM (The Bouncer - फक्त मोठ्यांची एन्ट्री)
# एक decorator बनवा adult_only. हा एका n (वय/age) घेणाऱ्या function ला wrap करेल.
# जर n >= 18 असेल, तरच function run करा.
# जर n < 18 असेल, तर print करा: "पोरकटपणा नको! एन्ट्री नाही."

def adult_only(func):
    def wrapper(n):
        if n >= 18:
            return func(n)
        else:
            print("Not valid..")
    return wrapper

@adult_only
def bouncer(n):
    print(f"The age is accepted : {n}")

bouncer(5)

# 4. MEDIUM (The Currency - पैसे दाखवणारा)
# एक decorator बनवा in_rupees. समजा तुझा function फक्त एक नंबर return करतोय (उदा. 500), तर decorator ने त्याच्या मागे ₹ जोडला पाहिजे.
# Output: ₹ 500



def in_rupees(func):
    def wrapper(n):
        func(n)
        print(f"₹ {n}")
    return wrapper

@in_rupees
def currency(n):
    print("The currency is valid.")

currency(50)





def triple_result(func):
    def wrapper(n):
        result = func(n) * 3
        return result
    return wrapper

@triple_result
def number(n):
    return n

print(number(10))




def only_even(func):
    def wrapper(num):
        if num % 2 == 0:
            return func(num)
        else:
            return "Odd numbers not allowed"
    return wrapper

@only_even
def n(num):
    return num

print(n(4))
print(n(5))



def add_stars(func):
    def wrapper():
        print("*****")
        func()
        print("*****")
    return wrapper

@add_stars
def greet():
    print("Learning Decorators")

greet()



def safe_divide(func):
    def wrapper(a, b):
        if b == 0:
            print("Cannot divide by zero")
        else:
           return func(a, b)
    return wrapper

@safe_divide
def divide(a, b):
    return a / b

print(divide(10, 2))
divide(10, 0)




# is_logged_in = True
def login_required(func):
    def wrapper(is_logged_in):
        if is_logged_in is True:
            func(is_logged_in)
        else:
            print("Please log in first...")
    return wrapper

@login_required
def dashboard(is_logged_in):
    print("Welcome to dashboard...")

dashboard(True)
dashboard(False)





def timer(func):
    def wrapper():
        print("Function is Starting...")
        func()
        print("Function is Finished...")
    return wrapper

@timer
def greeet():
    print("Hello")
greeet()





def reporter(func):
    def wrapper(a, b):
        print("I am doing process on a and b.")
        result = func(a, b)
        return result
    return wrapper

@reporter
def math(a, b):
    return a+b
print(math(2, 4))



def add_ten(func):
    def wrapper (a):
        result = func(a)
        new_result = result + 10
        return new_result
    return wrapper 
@add_ten
def math1(a):
    return a
print(math1(50))



def check_vip(func):
    def wrapper(user_name):
        if user_name == "Ketan":
            return func(user_name)
        else:
            print("Sorry, this is only for VIPs only..")
    return wrapper

@check_vip
def access_dashboard(user_name):
    return f"Welcome to the VIP dashboard, {user_name}"

print(access_dashboard("Ketan"))
print(access_dashboard("Rahul"))




def shout(func):
    def wrapper(a):
        return func(a).upper()        
    return wrapper

@shout
def shout_name(a):
    return a
print(shout_name("coding god"))