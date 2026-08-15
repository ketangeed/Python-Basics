def divide(a, b):
    try:
        # a = int(input("Enter the first number : "))
        # b = int(input("Enter the second number : "))
        print(a/b)

    except Exception as e:
        print("the error is occured...", e)

    finally:
        print("This is always executed...")

    # it always excuted no matter the if try executed or not...
    # finally:
    #     print("This is always executed...")

# a = int(input("Enter the first number : "))
# b = int(input("Enter the second number : "))

divide(10, 0)