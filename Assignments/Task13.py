# Fri, 3 Sep 2021
# Task 13
# Reading and writing csv file
import csv
def viewData():
    with open("D:\\College\\SEM 5\\Implant Training\\Git\\AI-ML-Inplant-Training\\Temp.csv", "rt") as f:
        for lines in csv.reader(f):
            print(lines)

def addData():
    with open("D:\\College\\SEM 5\\Implant Training\\Git\\AI-ML-Inplant-Training\\Temp.csv", "a", newline='') as f:
        lisToWrite = []
        lisToWrite.append(input("Enter Details :\n\t Employee Id : "))
        lisToWrite.append(input("\t        Name : "))
        lisToWrite.append(input("\t  Department : "))
        lisToWrite.append(input("\t      Salary : "))
        lisToWrite.append(input("\t  Experience : "))
        w = csv.writer(f)
        w.writerow(lisToWrite)

def main():
    ch = int(input("Press\n1. View Data\n2. Add Student\n3. Exit\n\tSelect : "))
    if ch == 1:
        viewData()
        main()
    elif ch == 2:
        addData()
        main()
    elif ch == 3:
        exit()
    else:
        print("Invalid Choice !!!")
        main()

main()