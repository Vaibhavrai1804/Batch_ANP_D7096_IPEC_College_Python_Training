#earch Student Using Function

# Function to search student by roll number
def search_student(student_dict, roll_no):

    if roll_no in student_dict:
        return student_dict[roll_no]
    else:
        return "Student Not Found"


# Main Program

student_dict = {}

print("Enter details of 5 students:")
for i in range(5):
    roll_no = int(input("Enter Roll Number: "))
    name = input("Enter Student Name: ")
    student_dict[roll_no] = name

search_roll = int(input("\nEnter Roll Number to Search: "))

# Function Call
result = search_student(student_dict, search_roll)

# Display Result
print("Result :", result)