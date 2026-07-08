#Create a dictionary to store the marks of 5 students, where the key is the student's name and the value is their marks. 
students = {
    "Aarav": 85,
    "Priya": 92,
    "Rohan": 78,
    "Sneha": 95,
    "Kabir": 88
}
# Display all student names and marks.  
for i in students:
    print(i,"->",students[i])


# #Add a new student with marks.  
# name=input("Enter name of student : ")
# mark=int(input("Enter marks :"))
# students[name]=mark
# print("Updated data :",students)

#Update the marks of an existing student.

# name2=input("Enter name of student which marks has to be updated: ")
# flag=False
# for i in students:
#     if i==name2:
#         flag=True
# if flag==True:
#     mark2=int(input("Enter updated marks :"))
#     students[name2]=mark2
#     print("Updated data :",students)
# else:
#     print("Given name is not present in the record")

# Delete a student by name.  

name3 = input("Enter name which should be deleted: ")

if name3 in students:
    del students[name3]
    print("Updated data is:", students)
else:
    print("Given name is not present in the data")
#Display the student who scored the highest marks
high=0
top_student=""
for i in students:
    if students[i]>high:
        high=students[i]
        top_student=i
print(top_student,"scored",high,"marks which is highest amongst all the student ")
