# Check Password Strength Using Function

# Function to check password strength
def check_password(password):

    upper = False
    lower = False
    digit = False

    # Check each character
    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True

    # Check all conditions
    if len(password) >= 8 and upper and lower and digit:
        return "Strong Password"
    else:
        return "Weak Password"


# Main Program
password = input("Enter Password: ")

result = check_password(password)

print("Result :", result)