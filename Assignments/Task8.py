# Mon, 23 Aug 2021
# Task 8.1
# Take input from user and find out sum and average of 0 to that number.

i =0
sum = 0
n = int(input("\nEnter number : "))
while i <= n :
	sum+= i
	i += 1
print("------------------------------------------")
print(f"\nSum of numbers from 0 to {n} = {sum} ")
print(f"                 & Average = {sum/n}")
print("------------------------------------------")

# Task 8.2
# Take a number as input and print multiplication table of that number using while loop.
print("\nTable of ", n)
i = 0
while i <= 10 :
	print(f"{n} * {i} = {i*n}")
	i += 1
print("------------------------------------------")

# Task 8.3
# Writr a program to find factorial using while loop.
fact = 1
i = 1
while i <= n :
	fact *= i 
	i += 1
print(f"\n Factorial of {n} : ", fact)
print("------------------------------------------")