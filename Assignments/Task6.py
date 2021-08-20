# Fri, 20 Aug 2021

# Task 6.1
# Take input from user and check given input is odd or even.
if int(input("Enter a number :"))%2 == 0 :
	print("Number is even")
else:
	print("Number is odd")

print("--------------------------------------")



# Task 6.2
# Take input of age of 3 people by user and determine oldest and youngest among them.
age1 = float(input("\n Enter Age of First Person : "))
age2 = float(input("\n Enter Age of Second Person : "))
age3 = float(input("\n Enter Age of Third Person : "))
print("")

if age1 == age2 and age1 != age3:
	if age1 > age3:
		print("First and Second person are older than third")
	else :
		print("Third person is older than other two")
elif age2 == age3 and age2 != age1 :
	if age2 > age1:
		print("Second and Third person are older first")
	else :
		print("First person is older than other two")
elif age3 == age1 and age3 != age2 :
	if age3 > age2:
		print("First and Third person are older second")
	else :
		print("Second person is older than other two")
else :
	if age2<=age1>=age3 :
		print("First person is older than other two")
	elif age1<=age2>=age3:
		print("Second person is older than other two")
	elif age1<=age3>=age2 :
		print("Third person is older than other two")
	else :
		print("All have same age!!")

	if age2>=age1<=age3 :
		print("First person is younger than other two")
	elif age1>=age2<=age3 :
		print("Second person is younger than other two")
	elif age1>=age3<=age2 :
		print("Third person is younger than other two")
	else :
		print("All have same age!!\n")

print("--------------------------------------")



# Task 6.3
# Simple program to calculate area of squares whose sides are given in a list. side = [5,4,7,8,9,3,8,2,6,4]
side=[5, 4, 7, 8, 9, 3, 8, 2, 6, 4]
print("\nlength of side        Area of square ")
for i in side : print(f"\t {i}       \t {i*i}")