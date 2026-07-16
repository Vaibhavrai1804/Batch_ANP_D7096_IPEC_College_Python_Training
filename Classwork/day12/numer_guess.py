secret_number = 57
attempts = 0
max_attempts = 7

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))

    # Ignore negative numbers
    if guess < 0:
        print("Negative numbers are not allowed!")
        continue

    attempts += 1

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        print("Attempts used:", attempts)
        break
    elif guess < secret_number:
        print("Too Low!")
    else:
        print("Too High!")

else:
    print("Sorry! You have used all 7 attempts.")
    print("The secret number was:", secret_number)
    print("Attempts used:", attempts)

#-------------------OUTPUT----------------------
'''
Enter your guess: 55
Too Low!
Enter your guess: 54
Too Low!
Enter your guess: 155
Too High!
Enter your guess: 57
Congratulations! You guessed the correct number.
Attempts used: 4
'''