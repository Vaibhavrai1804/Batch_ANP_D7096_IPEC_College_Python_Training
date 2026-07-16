password = input("Enter Password: ")

missing = []

# Minimum length
if len(password) < 8:
    missing.append("Minimum 8 characters")

# Uppercase check
has_upper = False
for ch in password:
    if ch.isupper():
        has_upper = True
        break

if not has_upper:
    missing.append("At least one uppercase letter")

# Lowercase check
has_lower = False
for ch in password:
    if ch.islower():
        has_lower = True
        break

if not has_lower:
    missing.append("At least one lowercase letter")

# Digit check
has_digit = False
for ch in password:
    if ch.isdigit():
        has_digit = True
        break

if not has_digit:
    missing.append("At least one digit")

# Special character check
has_special = False
for ch in password:
    if not ch.isalnum():
        has_special = True
        break

if not has_special:
    missing.append("At least one special character")

# Final Result
if len(missing) == 0:
    print("Strong Password")
else:
    print("Weak Password")
    print("Missing Conditions:")
    for item in missing:
        print("-", item)