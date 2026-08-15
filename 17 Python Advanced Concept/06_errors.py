# try and except statements are used to handle errors in python. just wrap the program inside the try and except and they will take care of it.

# whenever there is an error the code inside the except block is executed and the program dosen't crash.
# if there is no error the code in try will executed..


while True:

    try:
        a = int(input("Enter the first number : "))
        b = int(input("Enter the second number : "))

        print(f"The division is {a//b}")
    
    except Exception as e:
        print("the error is occured!!!", e)
    
    except ZeroDivisionError:
        print("Don't divide it by zero...")

    except ValueError:
        print("hey, don't perform the bad typecast.")
    

    # now this is the syntax to get that exception...
    # except:
    #     print("the error is occured!!!")





a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

print(f"The division is {a//b}")
if b == 0:
    raise ValueError("don't divide the value by zero.")
print(f"The division is {a//b}")

# we've made the customized error....
# we've raised the exception...