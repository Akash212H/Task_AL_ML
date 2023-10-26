#CTAS :CREATE-TABLE-AS -SELECT--------->table to table copy

import pymysql

con=pymysql.connect(host="localhost",user="__",password="__",database="mydb21")

#Creating a cursor object

cur1=con.cursor()

cur1.execute("create table emp3 as select * from emp")

cur1.execute("select * from emp3")

for row in cur1:
    print(row)

cur1.close()
con.close()

