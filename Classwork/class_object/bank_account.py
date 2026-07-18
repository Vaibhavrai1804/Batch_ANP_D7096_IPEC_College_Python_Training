class BankAccount:
    def __init__(self):
        self.account_number = ""
        self.customer_name = ""
        self.balance = 0

    # Accept account details
    def accept_details(self):
        self.account_number = input("Enter Account Number: ")
        self.customer_name = input("Enter Customer Name: ")
        self.balance = float(input("Enter Initial Balance: "))

    # Deposit money
    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited Successfully!")

    # Withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn Successfully!")
        else:
            print("Insufficient Balance")

    # Display account details
    def display_balance(self):
        print("\n----- Account Details -----")
        print("Account Number :", self.account_number)
        print("Customer Name  :", self.customer_name)
        print("Current Balance:", self.balance)


# Create object
account = BankAccount()

# Accept details
account.accept_details()

# Deposit
deposit_amount = float(input("Enter Deposit Amount: "))
account.deposit(deposit_amount)

# Withdraw
withdraw_amount = float(input("Enter Withdrawal Amount: "))
account.withdraw(withdraw_amount)

# Display final balance
account.display_balance()

#----------------OUTPUT---------------------
'''
CASE 1: Sufficient Balance 
Enter Account Number: 1001
Enter Customer Name: Anjali
Enter Initial Balance: 5000
Enter Deposit Amount: 2000
Amount Deposited Successfully!
Enter Withdrawal Amount: 4500
Amount Withdrawn Successfully!

----- Account Details -----
Account Number : 1001
Customer Name  : Anjali
Current Balance: 2500.0
-------------------------------------------------

CASE 2: insufficient Balance 
Enter Account Number: 1001
Enter Customer Name: Anjali
Enter Initial Balance: 5000
Enter Deposit Amount: 2000
Amount Deposited Successfully!
Enter Withdrawal Amount: 9000 
Insufficient Balance

----- Account Details -----
Account Number : 1001
Customer Name  : Anjali
Current Balance: 7000.0

'''