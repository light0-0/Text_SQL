import sqlite3

#connect 
connection = sqlite3.connect("student.db")

#create a Cursor Object to insert data,record table

cursor = connection.cursor()

#create table
table_info = """
Create Table STUDENT(NAME VAECHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25));
"""

cursor.execute(table_info)

#insert records 

cursor.execute(''' Insert Into STUDENT values('Hardik','COMPS','A')''')
cursor.execute(''' Insert Into STUDENT values('Vansh','IT','B')''')
cursor.execute(''' Insert Into STUDENT values('Priyanka','COMPS','A')''')
cursor.execute(''' Insert Into STUDENT values('Karan','IT','B')''') 
cursor.execute(''' Insert Into STUDENT values('Akshay','BIOMED','D')''')
cursor.execute(''' Insert Into STUDENT values('Priyanshu','Finance','F')''')
cursor.execute(''' Insert Into STUDENT values('Hardik','COMPS','A')''')
cursor.execute(''' Insert Into STUDENT values('Aaryan','IT','B')''')
cursor.execute(''' Insert Into STUDENT values('Vishwas','BIOMED','D')''')
cursor.execute(''' Insert Into STUDENT values('Rohit','CHEMICAL','C')''')

#display the records

print("The inserted records are")
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)


##Comit Your Changes into  the Database
connection.commit()
connection.close()