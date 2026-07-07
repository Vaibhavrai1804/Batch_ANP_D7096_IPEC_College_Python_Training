#Find Maximum, Minimum and Average Using Functions

# Function to find maximum value
def find_max(numbers):
    maximum = numbers[0]
    for i in numbers:
        if i > maximum:
            maximum = i
    return maximum


# Function to find minimum value
def find_min(numbers):
    minimum = numbers[0]
    for i in numbers:
        if i < minimum:
            minimum = i
    return minimum


# Function to find average
def find_average(numbers):
    total = 0
    for i in numbers:
        total = total + i
    average = total / len(numbers)
    return average


# Main Program
numbers = []

print("Enter 10 integers:")
for i in range(10):
    num = int(input("Enter number {}: ".format(i + 1)))
    numbers.append(num)

# Function Calls
maximum = find_max(numbers)
minimum = find_min(numbers)
average = find_average(numbers)

# Display Results
print("\nList :", numbers)
print("Maximum Value :", maximum)
print("Minimum Value :", minimum)
print("Average :", average)