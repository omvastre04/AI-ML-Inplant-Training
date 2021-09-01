# Wed, 1 Sep 2021
# Task 12.1
# WAP to check whether file exits or not, if exits then print content.

import os
fname = input("Enter File Name to check whether file exits or not : ")
if os.path.isfile(fname):
    print("File is present and the content in file is as follows : \n")
    with open(fname, "rt") as f:
        # for lines in f.readlines(): print(lines, end="")
        print(f.read())
else :
    print("File is not present")
print("------------------------------------------------------------------------------------------------------")


# Task 12.2
# Describe functions file
print("\n  Function    :  Usage\n")

print(".close()      :  Closes the file opened file")
print(".read()       :  Reads all over file")
print(".readable()   :  Tells whether the file stream can be read or not")
print(".readline()   :  Reads one line from the file")
print(".readlines()  :  Returns a list of lines from the file")
print(".seek()       :  Change the position of control")
print(".tell()       :  Tells the position of control")
print(".truncate()   :  Removes all over content in the file")
print(".writable()   :  Tells whether the file stream can be written or not")
print(".write()      :  Writes the specified string to the file")
print(".writelines() :  Writes a list of strings to the file")
print("------------------------------------------------------------------------------------------------------")
