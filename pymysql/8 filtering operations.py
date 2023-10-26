#filtering operations:

import pymysql

con=pymysql.connect(host="localhost",user="__",password="__",database="mydb21")


cur1=con.cursor()

#Filter those emps whose salaries are above 60000

cur1.execute("select * from emp where sal>60000")

for row in cur1:
    print(row)
print("\n")
#------------------------------------------------------------------------------------------
#2)Filter only male emp records
cur1.execute("select * from emp where sex='m'")

for row in cur1:
    print(row)
print("\n")
#-----------------------------------------------------------------------------------------
#3)Filter those whose sal>60000 and dno is 12
cur1.execute("select * from emp where sal>60000 and dno=12")

for row in cur1:
    print(row)
#-------------------------------------------------------------------------------------------

cur1.execute("select * from emp")

for row in cur1:
    print(list(row))
print("\n")
#-------------------------------------------------------------------------------------------
cur1.execute("select * from emp")

list1=[ ]

for row in cur1:
    list1.append(list(row))
print(list1)

list1[2][2]=75000
print(list1)

cur1.close()

con.close()


