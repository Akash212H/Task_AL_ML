
#Creating multiple cursor objects
'''
cur1---->for creating table
cur2---->for inserting data
cur3---->for retrieving data
'''
import pymysql

con=pymysql.connect(host="localhost",user="__",password="__",database="mydb21")

#Creating cur1 object for creating table
cur1=con.cursor()

#cur1.execute("create table emp(eid int,ename varchar(10),sal int,sex varchar(1),dno int,city varchar(10))")

#Creating cur2 object for inserting data
cur2=con.cursor()
cur2.execute("insert into emp values(101,'Miller',50000,'m',11,'pune'),(102,'Blake',60000,'m',12,'pune'),(103,'Sony',70000,'f',11,'hyd'),(104,'Priya',80000,'f',12,'hyd'),(105,'James',90000,'m',13,'hyd')")
con.commit() #for permanently saving

#Creating cur3 object for retrieving data
cur3=con.cursor()
cur3.execute("select * from emp")

#The o/p of the sql query is stored within the cur3 object

#using for loop we will retrieve one by one record

for row in cur3:
    print(row)

cur1.close()
cur2.close()
cur3.close()

con.close()


#Note: we can perform all the above operations using single cursor object also

#when to go for multiple cursor objects??

#cur1.execute("select * from emp")

#here emp data is stored in cur1 object

#cur1.execute("select * from customer")

#here customer data overwrites the emp data

#if i want both customer and emp data-->then create 2 cursor objects which stores the data


















