# decorator is a function, that takes another function as an argument, it creates the new function inside its body (wrapper). Then it returns that new function.
# takes function as an argument, and returns function.

# Decorator म्हणजे काय? एक प्रकारचा 'Wrapper' आहे.
# समजा तुझा एक साधा Function आहे जो फक्त "Hello" बोलतो. तुला त्या Function मध्ये बदल न करता, त्याच्या आधी आणि नंतर काहीतरी "Extra" काम करायचं आहे (उदा. टाळ्या वाजवणे किंवा नाव विचारणे).
# Asli Logic: Function च्या बाहेरून एक 'कव्हर' चढवणे. बिना function को छेड़े उसके behavior को upgrade करना।



# def decorator(func):
#     def wrapper():
#         print("Transction initiated.")
#         func()
#         print("Transction completed.")
#     return wrapper

# @decorator  
# def hello():
#     print("...include all the parameters of transaction... ")
# # hello()

# hello1 = decorator(hello) 
# # this takes lot of time so to stop this use the @ method on decorator. like above.
# hello1()




# def thank_you(func):
#     def wrapper(name):
#         print(f"thank you for showing up today {name}")
#         # result = func()
#         # return result
#         return func()
#     return wrapper

# @thank_you
# def show():
#     return "Learning is completed.."
# print(show("Ketan"))


 

def make_loud(func):
    def wrapper():
        # result = func()
        return func().upper()
    return wrapper

@ make_loud
def greet():
    return "Hello..."
        
print(greet())



