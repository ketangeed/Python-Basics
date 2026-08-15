# it is used when you want to match a value with many possible cases
# Use match-case when matching exact values.
# If there is comparison → use if-elif.
# Use match-case when:
# exact value matching
# menu systems
# fixed commands
# numbers or strings

a = int(input("Enter the Lucky Number between 1 and 10 : "))

match a :
    case 1:
        print("you won a car.")
    case 4:
        print("you won a bike.")
    case _:
        print("Better luck Next time.")


# colour = int(input("Enter the number between (1-3) : "))

# match colour:
#     case 1 :
#         print("Red")
#     case 2 :
#         print("Blue")
#     case 3 :
#         print("Green")
#     case _:
#         print("Invalid Colour.")



a = float(input("Enter the first number : "))
b = float(input("Enter the second number : "))
op = input("Enter the Operations from this  (+,-,*,/)  :- ")

match op:
    case "+":
        print(f"Result is {a+b}")
    case "-":
        print(f"Result is {a-b}")
    case "*":
        print(f"Result is {a*b}")
    case "/":
        if b != 0:
            print(f"Result is {a//b}")

        else:
            print("it is not divisible by 0.")
    case _:
        print("Invalid Number.")
      
       
      
    
    
num1 = int(input("Enter the 1st number : "))
num2 = int(input("Enter the 2nd number : "))
op = input("Enter the operation (+,-,*,/) :")

match op :
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 // num2)
    case _:
        print("Invalid.")