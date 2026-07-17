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
sql_query='select * from Student'

#-----------------------------------------
#to execute the query
cursorobj.execute(sql_query)
# data=cursorobj.fetchall() #Tis stores data in memory hence less performance

#---------------------------
#To fetch the data 
data=False 
for row in cursorobj:
    data=True
    print("Student ID :",row[0])
    print("Student Name :",row[1])
    print("Standard:",row[2])
    print("Age :",row[3],"year")
    print("----------------------------")
#---------------------------------------
if data==False:
    print("No data found")


# #-----------------------------------
# #To check data inserted or not 
# if (len(data)>0):
#     print("Data fetched Sucessfully")
# else:
#     print("Data not fetched")
# #-----------------------------------------


#To close the cursor connection
cursorobj.close()

#--------------------
#To close the connection object
dataconnection.close()


#--------------------OUTPUT----------------
'''
Student ID : std101
Student Name : Anil
Standard: 11th
Age : 16 year
----------------------------
Student ID : std103
Student Name : Rahul
Standard: 9th
Age : 14 year
----------------------------
Student ID : std104
Student Name : Mohit
Standard: 12th
Age : 17 year
----------------------------
Student ID : std105
Student Name : Rohit
Standard: 8th
Age : 13 year
----------------------------
'''