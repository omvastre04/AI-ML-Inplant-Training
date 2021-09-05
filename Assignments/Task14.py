import mysql.connector

# Connect to host
mydb = mysql.connector.connect(host="localhost", user="main", password="")
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

