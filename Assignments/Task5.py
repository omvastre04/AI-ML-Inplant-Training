# Thu, 19 Aug 2021

# Task 5.1
# Examples of Bitwise Operators
print("\nBitwise Operation :")
x=10
y=20
print(f"x=10, y=20")

print("\n     Operator    Operation   Result\n")
print("      And (&)     x  &  y    ", x&y)
print("       OR (|)     x  |  y    ", x|y)
print("      XOR (^)     x  ^  y    ", x^y)
print("      Not (~)        ~  y    ",  ~y)
print(" R Shift (>>)     x >>  y    ", x>>y)
print(" L Shift (<<)     x <<  y    ", x<<y)

print("----------------------------------------------")

# Task 5.2
# Examples of Membership Operators
print("\nMembership Operators :")

list1=[10, 20, 30, 40]
print("List = ", list1)

print("\n     Operator    Operation        Result\n")
print("           in    10 in List      ", 10 in list1)
print("       not in    10 not in List  ", 10 not in list1)

a="abc"
b=20
print("\n a = abc, b=20")

print("     Operator    Operation    Result\n")
print("           is    a is b      ", a is b)
print("       is not    a is not b  ", a is not b)
