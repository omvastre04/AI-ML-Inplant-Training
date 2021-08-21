# Sat, 21 Aug 2021
# Task 7.1
# To print multiplication table of given number. n=5
print("\n Task 7.1")
n=int(input("Enter number to get it's table : "))
for i in range(11): print(f"{n} * {i} = {n*i}")

# Task 7.2
# To check whether a character is an alphabet or not.
print("\n Task 7.2")
n=input("Enter to check whether is it character or not : ")
if n[0].isalpha(): print(f"{n} is a character.")
else: print(f"{n} is not a character.")

# Task 7.3
# Display numbers from 30 to 10 using for loop
print("\n Task 7.3")
for i in range(30, 10, -1):print(i, end=" ")

# Task 7.4
# To check Vowel or Consonant.
print("\n Task 7.4")
a=input("\nEnter character to check vowel or consonant : ")
if a in ['a', 'e', 'i', 'o', 'u'] :
    print(f"{a} is Vowel")
else:
    print(f"{a} is Consonant")

# Task 7.5
# A school has following rules for grading system:
# Below 25 - f, 25 to 45 - e, 45 to 50 - d, 50 to 60 - c, 60 to 80 - b, above 80 - a
print("\n Task 7.5")
marks = int(input("Enter Marks : "))
if marks<=25 : print("Your Grade is 'F' ")
elif 25<marks<=45 : print("Your Grade is 'E' ")
elif 45<marks<=50 : print("Your Grade is 'D' ")
elif 50<marks<=60 : print("Your Grade is 'C' ")
elif 60<marks<=80 : print("Your Grade is 'B' ")
elif 80<marks : print("Your Grade is 'A' ")
else: print("Invalid Input!!!")