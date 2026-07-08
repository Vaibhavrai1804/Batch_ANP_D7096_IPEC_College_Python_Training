#Create a nested dictionary to store marks of students in three subjects. 
#Taking input of number of students 
n=int(input("Enter number of students :"))
student_data={}
marks={}
for i in range(n):
    print("Student",(i+1))
    name=input("Enter name of student :")
    for j in range(3):
        print("Subject",j+1)
        subject=input("Enter subject name :")
        mark=int(input("Enter marks : "))
        marks[subject]=mark
    student_data[name]=marks
    marks={}
print(student_data)

#----------------------------------------------
print("------------------------------------------")

# Calculate the total marks of each student.
total_mark=0
for i in student_data:
    for j in i:
        total_mark+=i[j]
        
    print("Total mark of ",i,"is:",total_mark)
    total_mark=0



