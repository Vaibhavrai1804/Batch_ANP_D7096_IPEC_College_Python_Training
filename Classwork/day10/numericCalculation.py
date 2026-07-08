#Function for addition 
def calcualte_addition(a,b):
    return(a+b)

#---------------------------------------------
#Function for Subtraction 
def calcualte_difference(a,b):
    return(a-b)
#---------------------------------------------
#Function for multiplication
def calcualte_multiplication(a,b):
    return(a*b)

#---------------------------------------------
#Function for division 
def calcualte_division(a,b):
    if (b==0):
        print("Denominator can't be zero")
    else:
        return(a/b)
    
#---------------------------------------------
#Function for Modulus
def calcualte_remainder(a,b):
    return(a%b)
