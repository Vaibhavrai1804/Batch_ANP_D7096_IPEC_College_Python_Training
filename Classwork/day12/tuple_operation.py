# Tuple of 15 students
students = (
    "Aman", "Vaibhav", "Rahul", "Sagar", "Priya",
    "Anjali", "Riya", "Aman", "Neha", "Karan",
    "Rohit", "Simran", "Pooja", "Arjun", "Ritika"
)

# Total students
print("Total Students:", len(students))

# First five students
print("First Five Students:", students[:5])

# Last five students
print("Last Five Students:", students[-5:])

# Search a student
name = input("Enter student name to search: ")

if name in students:
    print(name, "is present in the tuple.")
else:
    print(name, "is not present in the tuple.")

# Count occurrences
count = students.count(name)
print("Occurrences of", name, ":", count)

# Convert tuple to list and sort
student_list = list(students)
student_list.sort()

print("Sorted Student List:")
print(student_list)