import mysql.connector
# To establish the connection with mysql
dataconnection=mysql.connector.connect(
    host='localhost',user='root',password='Vaibhav@2005',database='StudentManagement'
)
#To check whether it is connected or not 
print("Connected")

#to create a cursor object
cursorobj=dataconnection.cursor()

#Writing insert query
sql_query='insert into Student values(%s,%s,%s,%s)'

#-------------------------------------
stdid='std101'
stdname='Anil'
standard='10th'
age=15
#put the values to be inserted on tuple
values=(stdid,stdname,standard,age)
#-----------------------------------------
#to execute the query
cursorobj.execute(sql_query,values)

#To commit the changes
dataconnection.commit()

#-----------------------------------
#To check data inserted or not 
if (cursorobj.rowcount>0):
    print("Data inserted Sucessfully")
else:
    print("Data not inserted")
#-----------------------------------------

#To close the cursor connection
cursorobj.close()

#--------------------
#To close the connection object
dataconnection.close()


#----------------OUTPUT--------------
'''
mysql> Select *
    -> from Student;
+--------+---------+----------+-----+
| StdId  | StdName | Standard | age |
+--------+---------+----------+-----+
| std101 | Anil    | 10th     |  15 |
+--------+---------+----------+-----+
'''
    