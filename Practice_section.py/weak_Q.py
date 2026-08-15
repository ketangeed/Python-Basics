# # q.1) 5 star pattern

# for i in range(1, 6):
#     print("*"*i)

# # q.2) number pattern

# for i in range(1, 5):
#     for j in range(1, i+1):
#         print(j, end="")
#     print()

# for i in range(5, 0, -1):
#     s = "12345"
#     print(s[:i])


# for i in range(6, -1, -1):
#     s = "PYTHON"
#     print(s[i:])



# for i in range(1, 6):      # 1. THE BOSS: Tells the worker which number to stamp
#     for j in range(i):     # 2. THE WORKER: Repeats the job 'i' times per row
#         print(i, end="")   # 3. THE STAMP: Prints the Row Number, stays on same line
#     print()                # 4. THE ENTER KEY: Moves to next row when worker finishes


# # =================================================================
# # Q4: THE ALIGNED TRIANGLE (SPACES + STARS)
# # =================================================================
# # LOGIC: You are printing TWO things before hitting 'Enter'.
# # Row 1: [Space, Space, Space, Space, Star]
# # Row 2: [Space, Space, Space, Star, Star]

# n = 5
# for i in range(1, n + 1):
#     # 1. THE SPACE BAR: Prints leading spaces to push stars to the right.
#     # Formula: Total Rows (5) minus Current Row (i).
#     for j in range(n - i):
#         print(" ", end="") 
        
#     # 2. THE STAR STAMPER: Prints the stars immediately after spaces.
#     # Formula: Exactly 'i' stars for Row 'i'.
#     for k in range(i):
#         print("*", end="")
        
#     # 3. THE RESET: Move to the next line only after Spaces AND Stars are done.
#     print()

# # -----------------------------------------------------------------
# # PRO-TIP (THE "PYTHONIC" WAY):
# # Instead of two inner loops, use String Multiplication:
# # print(" " * (n - i) + "*" * i)
# # =================================================================

# n = 5
# for i in range(1, n+1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(i):
#         print("*", end="")
#     print()
    

# # OR
# n = 8
# for i in range(1, n+1):
#     print(" " * (n - i) + "*" * i)




# n = 5
# for i in range(n, 0, -1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(i):
#         print("*", end="")
#     print()
    
    
# 1
# 21
# 321
# 4321


# for i in range(1, 6):
#     for j in range(i, 0, -1):
#         print(j, end="")
#     print()



# =================================================================
# Q6: THE BACKWARD COUNTDOWN TRIANGLE
# =================================================================
# LOGIC: The Inner Loop depends on the Outer Loop's CURRENT value.
# The 'start' of the inner range is 'i', and it stops at 0 (to include 1).

# for i in range(1, 5):
#     # INNER LOOP: range(start, stop, step)
#     # start = i (the row number)
#     # stop  = 0 (so it includes 1)
#     # step  = -1 (counting backwards)
#     for j in range(i, 0, -1):
#         print(j, end="")
#     print()

# 💡 WHY THIS WORKS:
# When i=3, the inner loop is range(3, 0, -1).
# This gives the numbers 3, 2, 1.
# =================================================================





# "aab" → a=2, b=1


# txt = "aab"
# count = 0
# count1 = 0
# for char in txt:
#     if char == "a":
#         count += 1
#     elif char == "b":
#         count1 += 1

# print("a =",count)
# print("b =",count1)






# STRINGS

text = input("Enter the text : ")
vowels = ['a','e','i','o','u']
count = 0
for char in text.lower():
    if char in vowels:
        count += 1
print(f"the count of the vowels is : {count}")