def process_data(value):
    print("🔌 Opening data connection...")

    try :
        result = 100 /  value

    except ZeroDivisionError :
        print("Cannot Divide By Zero.")

    else :
        return f"The Result is {result}"
    
    finally:
       print( "🧼 Closing data connection cleanly.")
    

print(process_data(10))
print(process_data(0))