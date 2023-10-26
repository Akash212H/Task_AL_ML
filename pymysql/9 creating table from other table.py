#Creating a table from another table

import pymysql

con=pymysql.connect(host="localhost",user="__",password="__",database="mydb21")

#Creating a cursor object

cur1=con.cursor()

cur1.execute("create table emp2 like emp")

#inserting data from one table to other i.e from emp  table to emp2 table
cur1.execute("insert into emp2 select * from emp")

con.commit()

cur1.execute("select * from emp2")

for row in cur1:
    print(row)

cur1.close()
con.close()





