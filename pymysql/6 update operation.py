
#update:

import pymysql

con=pymysql.connect(host="localhost",user="__",password="__",database="mydb21")

#Creating cur1 object for creating table
cur1=con.cursor()

cur1.execute("update emp set sal=sal+5000 where eid=102")

con.commit()

cur1.execute("select * from emp")

for row in cur1:
    print(row)

cur1.close()

con.close()
