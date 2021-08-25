# Wed, 25 Aug 2021
# Task 9.1
# pass a list to function and return sum of all items using function.
# Task 9.2
# write a program to reverse string using function.

def sum(inp):
    tot=0
    for i in inp:
        tot+=i
    return tot

def reverse_str(torev):
    return torev[::-1]

print(sum([8, 5, 6]))
print(reverse_str("abc"))
