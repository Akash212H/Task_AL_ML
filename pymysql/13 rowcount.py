

import pymysql

con = pymysql.connect(host='localhost',user='___',password='___',database='mydb21')
cur = con.cursor()
cur.execute("update emp set sal=sal+5000 where dno=12") #returns rowcount->2,if i give deptno=50,no rows affected
#cur.execute("select * from emp")  #returns rowcount--->0,as no records affected
con.commit()
print(cur.rowcount)
cur.close()
con.close()
#as in deptno 12,there r only 2 records,so 2 records affected,so 2 is returned


