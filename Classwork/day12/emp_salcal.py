# Function to calculate HRA
def calculate_hra(basic):
    return basic * 0.20

# Function to calculate DA
def calculate_da(basic):
    return basic * 0.10

# Function to calculate Tax
def calculate_tax(gross_salary):
    return gross_salary * 0.08

# Function to calculate Net Salary
def calculate_net_salary(basic):
    hra = calculate_hra(basic)
    da = calculate_da(basic)
    gross_salary = basic + hra + da
    tax = calculate_tax(gross_salary)
    net_salary = gross_salary - tax

    print("\n----- Salary Details -----")
    print("Basic Salary :", basic)
    print("HRA          :", hra)
    print("DA           :", da)
    print("Gross Salary :", gross_salary)
    print("Tax          :", tax)
    print("Net Salary   :", net_salary)

# Main Program
basic = float(input("Enter Basic Salary: "))
calculate_net_salary(basic)