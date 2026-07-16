text = input("Enter a string: ")

uppercase = 0
lowercase = 0
digits = 0
special = 0

frequency = {}

for ch in text:
    # Count character frequency
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

    # Count character types
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

# Find most frequent character
most_frequent = max(frequency, key=frequency.get)

# Display results
print("\n----- Character Analysis -----")
print("Uppercase Letters :", uppercase)
print("Lowercase Letters :", lowercase)
print("Digits            :", digits)
print("Special Characters:", special)
print("Most Frequent Character :", most_frequent)

#------------OUTPUT-------------
'''
Enter a string: Python@2026 

----- Character Analysis -----
Uppercase Letters : 1
Lowercase Letters : 5
Digits            : 4
Special Characters: 2
Most Frequent Character : 2
'''