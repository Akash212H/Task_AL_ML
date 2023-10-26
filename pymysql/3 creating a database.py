#Creating a database in mysql

import pymysql

con=pymysql.connect(host="localhost",user="___",password="___")


#Creating cursor object
cur1=con.cursor()  #here cur1 is the cursor object

#within this cursor object,we have execute() method, within which we can specify any valid
#sql query
cur1.execute("create database mydb21")

print("DATABASE CREATED SUCCESSFULLY!!!")

con.close()

cur1.close()
