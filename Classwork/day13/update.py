import mysql.connector
# To establish the connection with mysql
dataconnection=mysql.connector.connect(
    host='localhost',user='root',password='Vaibhav@2005',database='StudentManagement'
)
#To check whether it is connected or not 
print("Connected")

#Take input of student id
std_id=input("Enter Student ID :")
stu_age=int(input("Enter age of student :"))
standard=input("Enter Standard :")

#to create a cursor object
cursorobj=dataconnection.cursor()

#Writing update query
sql_query='update Student set age=%s,Standard=%s where StdId=%s'

#put the values to be inserted on tuple
values=(stu_age,standard,std_id)

#to execute the query
cursorobj.execute(sql_query,values)

#To commit the changes
dataconnection.commit()

#-----------------------------------------

#To close the cursor connection
cursorobj.close()

#--------------------
#To close the connection object
dataconnection.close()


#--------------OUTPUT-----------------
'''
Enter Student ID :std101
Enter age of student :16
Enter Standard :11th
mysql> select *
    -> from student;
+--------+---------+----------+-----+
| StdId  | StdName | Standard | age |
+--------+---------+----------+-----+
| std101 | Anil    | 11th     |  16 |
| std102 | Amit    | 11th     |  16 |
| std103 | Rahul   | 9th      |  14 |
| std104 | Mohit   | 12th     |  17 |
| std105 | Rohit   | 8th      |  13 |
+--------+---------+----------+-----+

'''
