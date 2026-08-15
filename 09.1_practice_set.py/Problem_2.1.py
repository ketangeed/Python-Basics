# ask user for 2 numbers and the operator and perform the operation using the match case.

a = int(input("Enter the First number : "))
b = int(input("Enter the second number : "))
c = input("Enter the operators (+, -, *, /) : ")

match c :
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)