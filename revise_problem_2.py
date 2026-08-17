# Takes a float input from the user for the price of an item (e.g., 19.99). Store it in a variable called price.

# Takes an integer input for the quantity of items being bought. Store it in a variable called quantity.

# Calculates the total cost (Price × Quantity) and stores it in a variable called total_cost.

# Prints the result using an f-string in this exact format:
# "Total cost for 3 items at $19.99 each is: $59.97" (using whatever values the user enters).


price = float(input("Enter the Price : "))
quantity = int(input("Enter the Quantity : "))
total_cost = price * quantity
print(f"Total cost for {quantity} items at {price} each is: {total_cost} ")

