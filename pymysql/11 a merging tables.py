#merging tables:

import pymysql

con=pymysql.connect(host="localhost",user="__",password="__",database="mydb21")

#Creating a cursor object

cur1=con.cursor()

cur1.execute("create table empres2 as select * from emp2 union all select * from emp3")

cur1.execute("select * from empres2")

for row in cur1:
    print(row)

cur1.close()

con.close()
