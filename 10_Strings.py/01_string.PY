name = "Ketan"  #can use double and single qoute in str.

name = 'Ketan'

name = '''Ketan''' # triple for the multiple strings.

print(name)


# =================================================================
# MASTERCLASS SUMMARY: STRING LOGIC & SLICING
# =================================================================

# 1. THE SLICE FORMULA: data[start : stop : step]
# RULE: "Include the Start, EXCLUDE the Stop."
# To get the first 5 chars, use [:5] (grabs index 0,1,2,3,4).

# 2. NEGATIVE INDEXING:
# Starts from -1 (the very last character).
# [-3:] means "Start 3 from the end and go to the finish."
# Example: "PYTHON"[-1] is 'N'.

# 3. THE RANGE EXCLUSION RULE:
# range(1, 6) gives 1, 2, 3, 4, 5 (Stops before 6).
# range(6, -1, -1) counts 6 to 0 (Stops before -1).
# USE: Set your 'stop' one step PAST what you want to include.

# 4. STEP PARAMETER [::x]:
# [::2] grabs every 2nd character (skips one).
# [::-1] reverses the entire string (steps backward).

# 5. DYNAMIC CLEANING:
# .strip()   -> Removes leading/trailing whitespace.
# .split("-")-> Cuts string into a LIST at every dash.
# .replace() -> Swaps specific text for something else.

# 6. THE "TYPEWRITER" CONTROLS:
# print(val, end="") -> Keeps cursor on the SAME line (no Enter).
# print()            -> Hits the "Enter" key (New Line).
# =================================================================