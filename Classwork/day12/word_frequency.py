# Function to count word frequency
def word_frequency(sentence):

    # Remove punctuation
    sentence = sentence.replace(".", "")
    sentence = sentence.replace(",", "")
    sentence = sentence.replace("!", "")
    sentence = sentence.replace("?", "")

    # Convert to lowercase
    sentence = sentence.lower()

    # Convert sentence into list of words
    words = sentence.split()

    # Create dictionary
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    # Display words in alphabetical order
    print("\nWord Frequencies:")
    for word in sorted(frequency):
        print(word, ":", frequency[word])

    # Find most repeated word
    most_repeated = max(frequency, key=frequency.get)
    print("\nMost Repeated Word:", most_repeated)


# Main Program
sentence = input("Enter a sentence: ")
word_frequency(sentence)