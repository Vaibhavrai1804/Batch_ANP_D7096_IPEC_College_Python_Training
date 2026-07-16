# Electricity Bill Calculator

units = int(input("Enter total units consumed: "))

# Calculate bill amount
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

final_bill = bill

# Apply surcharge if bill exceeds ₹2000
if bill > 2000:
    final_bill = bill + (bill * 0.05)

# Apply minimum bill condition
if final_bill < 500:
    final_bill = 500

# Display results
print("\n----- Electricity Bill -----")
print("Total Units       :", units)
print("Bill Amount       : ₹", bill)
print("Final Payable Amt : ₹", round(final_bill, 2))

#---------------OUTPUT------------------
'''
Enter total units consumed: 250

----- Electricity Bill -----
Total Units       : 250
Bill Amount       : ₹ 1700
Final Payable Amt : ₹ 1700'''