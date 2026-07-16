# Dictionary to store Roll No and Marks
students = {}

# Input details of 10 students
for i in range(10):
    roll = int(input("Enter Roll No: "))
    marks = int(input("Enter Marks: "))
    students[roll] = marks

# Find Topper
topper = max(students, key=students.get)
print("\nTopper Roll No:", topper)
print("Topper Marks:", students[topper])

# Find Average Marks
total = sum(students.values())
average = total / len(students)

print("Average Marks:", average)

# Students scoring above average
print("\nStudents Scoring Above Average:")
for roll, marks in students.items():
    if marks > average:
        print("Roll No:", roll, "Marks:", marks)

# Count failed students
failed = 0
for marks in students.values():
    if marks < 35:
        failed += 1

print("\nFailed Students:", failed)

# Display Grades
print("\nGrades:")
for roll, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 35:
        grade = "D"
    else:
        grade = "Fail"

    print("Roll No:", roll, "Marks:", marks, "Grade:", grade)