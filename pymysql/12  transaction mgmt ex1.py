


import pymysql
con=pymysql.connect(host='localhost',user='__',password='__',database='mydb21')
cur=con.cursor()
saccno=input("Enter SOURCE ACCOUNT NO:")      
daccno=input("Enter DESTINATION ACCOUNT NO:")
tamt=input("Enter TRANSFER AMOUNT:")
query1='update customer set bal = bal -'+tamt+' where accno='+saccno #removing from one account
print(query1)
query2='update customer set bal = bal +'+tamt+' where accno='+daccno #adding in another account
print(query2)

try:
    cur.execute(query1)
    cur.execute(query2)  #if any query gives error ctrl goes to except block (ex: if table doesn't exist)
    cur.close()
    con.commit() #here if bodth queries executes only perform commit(),else rollback()
    
except:
    con.rollback()
    print("Error")
    
con.close()

