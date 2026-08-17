# Prompts the user to enter their birth year using input() and stores it in a variable called birth_year.

# Converts birth_year into an integer and calculates their age assuming the current year is 2026. Store the result in a variable called age.

# Prints: "Your age is: X" (where X is the calculated age).


birth_year = input("Enter Your Birth Year : ")
b = int(birth_year)
age = 2026 - b
print(f"Your age is: {age}")