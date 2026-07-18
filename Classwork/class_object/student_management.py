#Problem 1: Student Management System 
class Student:
    student_id=0
    student_name=''
    course=''
    marks=0
    def initialize(self,id,name,c,m):
        self.student_id=id
        self.student_name=name
        self.course=c
        self.marks=m
    def check_result(self,marks):
        if (self.marks>35):
            return "Pass"
        else:
            return "Fail"
    def display_data(self):
        print("--------Student Details---------")
        print("Student ID :",self.student_id)
        print("Student name :",self.student_name)
        print("Course :",self.course)
        print("Marks :",self.marks)
        print("Result :",self.check_result(self.marks))
stu=Student()
i=int(input("Enter Student ID :"))
n=input("Enter Student name :")
co=input("Enter course :")
ma=int(input("Enter marks :"))
print("-----------------------------------")
stu.initialize(i,n,co,ma)
stu.display_data()


#--------------OUTPUT-----------------
'''
Enter Student ID :101
Enter Student name :Rahul
Enter course :Python
Enter marks :78
-----------------------------------
--------Student Details---------
Student ID : 101
Student name : Rahul
Course : Python
Marks : 78
Result : Pass
'''

    
