# List to store student records
students = []

# 1. Add Student
def add_student():
    roll = int(input("Enter Roll Number: "))

    # Check duplicate roll number
    for student in students:
        if student["Roll"] == roll:
            print("Roll Number already exists!")
            return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    student = {
        "Roll": roll,
        "Name": name,
        "Age": age,
        "Course": course,
        "Marks": marks
    }

    students.append(student)
    print("Student Added Successfully!")

# 2. Display All Students
def display_students():
    if len(students) == 0:
        print("No Records Found!")
        return

    for student in students:
        print(student)

# 3. Search Student
def search_student():
    roll = int(input("Enter Roll Number: "))

    for student in students:
        if student["Roll"] == roll:
            print(student)
            return

    print("Student Not Found!")

# 4. Update Marks
def update_marks():
    roll = int(input("Enter Roll Number: "))

    for student in students:
        if student["Roll"] == roll:
            student["Marks"] = float(input("Enter New Marks: "))
            print("Marks Updated Successfully!")
            return

    print("Student Not Found!")

# 5. Delete Student
def delete_student():
    roll = int(input("Enter Roll Number: "))

    for student in students:
        if student["Roll"] == roll:
            students.remove(student)
            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")

# 6. Display Topper
def display_topper():
    if len(students) == 0:
        print("No Records Found!")
        return

    topper = max(students, key=lambda x: x["Marks"])
    print("Topper:")
    print(topper)

# 7. Display Average Marks
def average_marks():
    if len(students) == 0:
        print("No Records Found!")
        return

    total = 0
    for student in students:
        total += student["Marks"]

    avg = total / len(students)
    print("Average Marks:", avg)

# 8. Students Above Average
def above_average():
    if len(students) == 0:
        print("No Records Found!")
        return

    total = 0
    for student in students:
        total += student["Marks"]

    avg = total / len(students)

    print("Students Above Average:")
    for student in students:
        if student["Marks"] > avg:
            print(student)

# Main Menu
while True:

    print("\n===== Student Record Management =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Display Topper")
    print("7. Display Average Marks")
    print("8. Display Students Above Average")
    print("9. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        display_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        update_marks()

    elif choice == 5:
        delete_student()

    elif choice == 6:
        display_topper()

    elif choice == 7:
        average_marks()

    elif choice == 8:
        above_average()

    elif choice == 9:
        print("Program Exited.")
        break

    else:
        print("Invalid Choice! Please Try Again.")