# Accept 20 integers
numbers = []

for i in range(20):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("\nOriginal List:", numbers)

# a) Largest number
print("Largest Number:", max(numbers))

# b) Second largest number
unique = list(set(numbers))
unique.sort()
print("Second Largest Number:", unique[-2])

# c) Smallest number
print("Smallest Number:", min(numbers))

# d) Remove duplicate elements
duplicates_removed = list(set(numbers))
print("List after removing duplicates:", duplicates_removed)

# e) Print even numbers
print("Even Numbers:")
for num in numbers:
    if num % 2 == 0:
        print(num, end=" ")

# f) Numbers divisible by both 3 and 5
print("\nNumbers divisible by both 3 and 5:")
for num in numbers:
    if num % 3 == 0 and num % 5 == 0:
        print(num, end=" ")

# g) Reverse the list without using reverse()
reversed_list = numbers[::-1]
print("\n\nReversed List:", reversed_list)