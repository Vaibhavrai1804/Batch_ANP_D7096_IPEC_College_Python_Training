''' Write a program to enter the salaries of N employees. The program should find and display:
Highest salary(along with their name)
Lowest salary(along with their name)
Average salary'''
# Note : Multiple Employees can hold highest or lowest salary 
#--------------------------------------------------------------------------
#Requirement -----------------------------------------------
# First of all take the number of employees(n) from the user 
# Create 2 blank list one is dedicated for Employee names , another one for their salaries 
# then by using for loop display highest,lowest salary along with their name & calculate average salary 
#--------------------------------------------------------------------------
#Programming 

                                             
#Create two blank list 


emp_name=[]
emp_salary=[]



#Take number of employees(n) from the user 
n=int(input("Enter number of employees : "))


#Take input of employees name and their salary from the user 
#Calculating average salary and finding highest and lowest salary 


total=0
high=None
low=None
high_name=[]
low_name=[]


for i in range(n):
    print("Employee",i+1)#Employee 1
    name=input("Enter name of employee : ")#Amit
    salary=int(input("Enter salary of employee : "))#50,000
    emp_name.append(name)#['Amit']
    emp_salary.append(salary)#[50000]
    total+=salary#total=50000
    #For highest salary 

    if high==None or salary>high:
        high=salary
        high_name=[name]
    elif salary==high:
        high_name.append(name)
    #for lowest salary

    if low==None or salary<low:
        low=salary
        low_name=[name]
    elif salary==low:
        low_name.append(name)
#Calculating average salary
average_salary=total/n
#-----------------------------------------
print("-------------------------------------------")
#Displaying Name and salary 

print("Name of employees are : ",emp_name)
print("Salary of employees are : ",emp_salary)
#-----------------------------------------------------
print("---------Result---------")

#Displaying Average , highest and lowest salary 

print("Average Salary : ",average_salary)
print("Highest Salary : ",high)
print("Employee(s) :", ", ".join(high_name))
print("Lowest Salary : ",low)
print("Employee(s) :", ", ".join(low_name))

