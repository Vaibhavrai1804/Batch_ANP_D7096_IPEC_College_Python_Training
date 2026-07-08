#Function to calculate simple interest
def Calculate_Simpleinterest(principal,rate,time):
    return (principal*rate*time)/100

#----------------------------------------------
#MAIN PROGRAM
principal=float(input("Enter principal(in Rs):"))
rate=float(input("Enter rate(in %):"))
time=int(input("Enter time(in years):"))
print("Simple Interest(in Rs):",Calculate_Simpleinterest(principal,rate,time))