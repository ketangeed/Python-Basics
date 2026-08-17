# Task:
# Write a Python script using a while True loop that:

# Keeps asking the user for input: user_input = input("Enter a string: ").

# If the user types "stop", use break to exit the loop immediately.

# If the user types "skip", use continue to skip printing and go straight to asking for the next input.

# For any other input, print: f"You entered: {user_input}".


while True:
    
    user_input = input("Enter a string: ")
    
    if user_input == "stop":
        break

    elif user_input == "skip":
        continue
    print(f"You entered: {user_input}")


