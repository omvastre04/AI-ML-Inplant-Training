# Mon, 16 Aug 2021

# Task 2.1
# Write a program to manuplate list data
# - declare list type which carry 10 elements
# - extract all list
# - extract index number 2 to 5
# - print list element reverse
# - using append, insert add element in list
# - clear a list

# - declare list type which carry 10 elements
list1 = [1, 2, 3, 4, "Sugar", "Wheat", 55.78, 8+7j, True, False]
print("List : ", list1)

# - extract all list
for i in list1:
    print(i,end=" ")
print("")

# - extract index number 2 to 5
print(list1[2:6])

# - print list element reverse
print(list1[::-1])

# - using append, insert add element in list
list1.append("Appended")
list1.insert(4,"Inserted")
print(list1)

# - clear a list
list1.clear()
print(list1)
print("---------------------------------------------------")



# Task 2.2
# Write a program to manuplate tuple data
# - declare tuple type which carry 10 elements
# - extract all tuple
# - use index and count function

# - declare tuple type which carry 10 elements
tup1 = (1, 2, 3, 4, "Sugar", "Wheat", 55.78, 8+7j, True, False)
print("Tuple : ", tup1)

# - extract all tuple
for i in tup1:
    print(i,end=" ")
print("")

# - use index and count function
print(tup1.index("Wheat"))
print(tup1.count(4))
print("---------------------------------------------------")