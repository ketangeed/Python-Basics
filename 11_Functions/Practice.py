def print_pattern():
    print("*****")

print_pattern()



def check_freezing():
    temp = 32
    if temp <= 32:
        print("Alert: Freezing Point!")
    else:
        print("N temp.")

check_freezing()



def greet_user(name, role):
    print(f"Hello {name}! Welcome to your role as a {role}")

greet_user("Ketan", "AIML Engineer.")



def count_vowels_in_word(word):
    vowels = "aeiou"
    count_vowel = 0
    for i in word.lower():
        if i in vowels:
            count_vowel += 1
    return count_vowel

total = count_vowels_in_word("python")
print(total)



add = lambda x: x + 10
print(add(10))




def count_up(current, target):
    if current > target:
        print("Done.")
        return
    else:
        print(current)
        count_up(current + 1, target)
        

count_up(1, 3)




def sum_up_to(n):
    if n == 1:
        return n
    else:
        return sum_up_to(n-1) + n


print(sum_up_to(5))





def fact(n):
    if n == 1 or n ==0 :
        return n
    else:
        return fact(n-1) * n
print(fact(5))


def sum(i):
    if i ==0:
        return i
    else:
        return sum(i-1) + i
print(sum(5))
