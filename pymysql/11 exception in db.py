
import pymysql
con=None  #if connection is not established,in con variable,None is stored
try:    #if connection is established,connection object is stored in con variable
    con=pymysql.connect(host='localhost',user='__',password=',database='mydb21')
    print("connection established") #if any mistake in connection,
    cursor=con.cursor()   #then except block is executed and prints DB error
    cursor.execute("select * from emp")
    for row in cursor:
        print(row)
    cursor.close()#the stmts within try block are resource allocation stmts
except:
    print("DB error occured")
finally:
    if con!=None:  #These 3 stmts are resource deallocation stmts (or)
        con.close() #resource release stmts
        print("connection closed")

        
        
