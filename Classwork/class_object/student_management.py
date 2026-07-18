#Problem 1: Student Management System 
class Student:
    def __init__(self):
        student_id=0
        student_name=''
        course=''
        marks=0

    #Accept detail by user
    def accept_data(self):
        self.student_id=int(input("Enter Student ID :"))
        self.student_name=input("Enter Student name :")
        self.course=input("Enter course :")
        self.marks=int(input("Enter marks :"))
        print("-----------------------------------")
    #Check if the student pass or fail
    def check_result(self,marks):
        if (self.marks>35):
            return "Pass"
        else:
            return "Fail"
    #To display the data of student
    def display_data(self):
        print("--------Student Details---------")
        print("Student ID :",self.student_id)
        print("Student name :",self.student_name)
        print("Course :",self.course)
        print("Marks :",self.marks)
        print("Result :",self.check_result(self.marks))

#Object Creation
stu=Student()


#Accept detail
stu.accept_data()

#Display the data 
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

    
