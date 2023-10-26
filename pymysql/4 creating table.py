#Creating a table in mysql

import pymysql

con=pymysql.connect(host="localhost",user="__",password="__",database="mydb21")

#Creating cursor object

cur1=con.cursor()

cur1.execute('create table student1(name varchar(10),marks int)')

print("TABLE CREATED SUCCESSFULLY!!!")

cur1.execute("insert into student1 values('Ajay',90),('Rahul',70)")

con.commit() #For permanently saving

print("DATA INSERTED SUCCESSFULLY!!!")

cur1.execute("select * from student1")

#The output of the sql query is stored within the cur1 object
#we retrieve one by one row using for loop

for row in cur1:
    print(row)

cur1.close()
con.close()
    






