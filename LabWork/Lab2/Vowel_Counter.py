#Count Vowels Using Function

# Function to count vowels
def count_vowels(text):

    count = 0

    for ch in text:
        if ch in "aeiouAEIOU":
            count = count + 1

    return count


# Main Program
sentence = input("Enter a Sentence: ")

# Function Call
result = count_vowels(sentence)

# Display Result
print("Total Number of Vowels :", result)