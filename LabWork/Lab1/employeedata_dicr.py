#Dictionary employee data example 

# Initially take the number of employees
n=int(input("Enter number of employees :"))
dict_1={}
dict_2={}

for i in range (n):
    print("Employee",(i+1))
    emp_id=int(input("Enter employee id: "))
    name=input("Enter employee name:")
    depart=input("Enter department :")
    salary=int(input("Enter salary of employee:"))
    dict_2[name]=depart,salary
    dict_1[emp_id]=dict_2
    dict_2={}

#Display all employee details. 
# for i in dict_1:
#     print(i,"->",dict_1[i])


#Search for an employee using Employee ID.

# id=int(input("Enter Employee id of desired employee :"))
# flag=False
# for i in dict_1:
#     if i==id:
#         print("Employee found")
#         print(dict_1[i])
#         flag=True
# if flag==False:
#     print("No such employee is found")

#Increase the salary of all employees by 10%.
dict_3={}
for i in dict_1:
    for i in dict_1(i):
        dict_3[i]=
