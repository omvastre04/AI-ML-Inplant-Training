# Sat, 4 Sep 2021
# Task 14
# Database Using Python
import mysql.connector

# Connect to host
mydb = mysql.connector.connect(host="localhost", user="main", password="5GL60GkAD(Szl.zV")
print(mydb)

# Creating cursor
mycursor = mydb.cursor()
print(mycursor)

# Create Database
mycursor.execute("CREATE DATABASE mydatabase")
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)

# Connecting to just created database
mydb = mysql.connector.connect(host="localhost", user="main", password="5GL60GkAD(Szl.zV", database="mydatabase")
print(mydb)

# Creating cursor of just created database
mycursor = mydb.cursor()

# Creating table
mycursor.execute("CREATE TABLE student (name VARCHAR(255), class VARCHAR(255), branch VARCHAR(255))")
for x in mycursor:
  print(x)

# Creating table and Primary Key
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# Ading primary key on existing table
mycursor.execute("ALTER TABLE student ADD COLUMN rollno INT AUTO_INCREMENT PRIMARY KEY")

# Inserting data into table
sql = "INSERT INTO student (name, class, branch) VALUES (%s, %s, %s)"
val = ("John", "FY", "CO")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

# Inserting multiple rows into table
sql = "INSERT INTO student (name, class, branch) VALUES (%s, %s, %s)"
val = [
  ('Peter', 'FY', 'ME'),
  ('Amy', 'FY', 'CE'),
  ('Hannah', 'FY', 'EE'),
  ('Michael', 'FY', 'ENTC'),
  ('Sandy', 'FY', 'IT'),
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

# Insert Record and returns id
sql = "INSERT INTO student (name, class, branch) VALUES (%s, %s, %s)"
val = ("Tony", "TY", "ENTC")
mycursor.execute(sql, val)
mydb.commit()
print("1 record inserted, ID:", mycursor.lastrowid)

# Display records using select command
mycursor.execute("SELECT * FROM student")
# .fetchall() fetches all rows from the last executed statement and The fetchone() method will return the first row of the resuls.
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# Displaying data in particular columns
mycursor.execute("SELECT name, class FROM student")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# Displaying record using select where command
sql = "SELECT * FROM student WHERE class='TY'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# Displaying record using Wildcard Characters
# Select records where the address contains the word "TY"
sql = "SELECT * FROM student WHERE class LIKE '%TY%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# Prevent SQL Injection by using Escape query values by using the placholder %s method 
sql = "SELECT * FROM student WHERE branch = %s"
adr = ("ME", )
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# Sort the result alphabetically by names
sql = "SELECT * FROM student ORDER BY name"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# Sort the result reverse alphabetically by names
sql = "SELECT * FROM students ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# Delete records by applying condition
sql = "DELETE FROM student WHERE class = 'TY'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

# Delete records by applying condition by preventing sql injection
sql = "DELETE FROM student WHERE branch = %s"
adr = ("EE", )
mycursor.execute(sql, adr)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

# Delete Table
sql = "DROP TABLE customers"
mycursor.execute(sql)

# Delete Table if exists
sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql)

# Update column in table using filter(where command)
sql = "UPDATE student SET class = 'FY' WHERE class = 'TY'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

# Update column in table using filter(where command) by preventing sql injection
sql = "UPDATE student SET class = %s WHERE class = %s"
val = ("TY", "FY")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

# Displaying limited records using LIMIT
mycursor.execute("SELECT * FROM student LIMIT 5")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# Displaying limited records strating from particular position using LIMIT and OFFSET
mycursor.execute("SELECT * FROM student LIMIT 5 OFFSET 2")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# Combining rows from two or more tables, based on a related column between them, by using a JOIN statement
# Refer  https://www.w3schools.com/python/python_mysql_join.asp  for better understanding!
