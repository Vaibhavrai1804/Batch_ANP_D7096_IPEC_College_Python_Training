#Importing the module 
from twodfigures import *
while True:
    #---------------------------------    
    #Displaying the menu to the user
    
    print("-------------------------")
    print("Enter 1 --> Square")
    print("Enter 2 --> Circle")
    print("Enter 3 --> Triangle")
    print("Enter 4 --> Rectangle")
    print("-------------------------")
    while True:
    
        #Ask for the choice by the user
        choice=int(input("Enter your desired choice : "))
        
        
        
        #Now ask for the required dimension according to the user's choice 
        #For square
        if choice==1:
            side=float(input("Enter side of square : "))
            break
        #For circle
        elif choice==2:
            radius=float(input("Enter radius of circle : "))
            break

        #For Triangle
        elif choice==3:
            a=float(input("Enter first side of triangle :"))
            b=float(input("Enter second side of triangle :"))
            c=float(input("Enter third side of triangle :"))
            break

            
        #For Rectangle
        elif choice==4:
            length=float(input("Enter length of rectangle :"))
            breadth=float(input("Enter breadth of rectangle :"))
            break

        #For Wrong entry
        else:
            print("Wrong Entry !!!!")
            continue
    
    
    #---------------------------------
    #Ask for the area or perimeter 
    
    
    print("-------------------------")
    print("Enter 1 --> Area")
    print("Enter 2 --> Perimter")
    print("-------------------------")

    while True:
            
        choice1=int(input("Enter Your choice : "))
        #For square 
        if choice==1:
            if choice1==1:
                print("Area of square is :",squarearea(side))
                break
            elif choice1==2:
                print("Perimter of square is :",squareperimeter(side))
                break
            else:
                print("Wrong choice entered")
                continue
        #For circle
        if choice==2:
            if choice1==1:
                print("Area of circle is :",circlearea(radius))
                break
            elif choice1==2:
                print("Perimter of cirle is :",circleperimeter(radius))
                break
            else:
                print("Wrong choice entered")
                continue
        #for triangle
        if choice==3:
            if choice1==1:
                print("Area of triangle is :",trainglearea(a,b,c))
                break
            elif choice1==2:
                print("Perimter of triangle is :",traingleperimeter(a,b,c))
                break
            else:
                print("Wrong choice entered")
                continue
        #for rectangle
        if choice==4:
            if choice1==1:
                print("Area of rectangle is :",rectanglearea(length,breadth))
                break
            elif choice1==2:
                print("Perimter of rectangle is :",rectangleperimeter(length,breadth))
                break
            else:
                print("Wrong choice entered")
                continue
    print("Enter Yes if you want to conitnue the program ")
    print("Enter No if you want to exit the program ")
    choice2=input("Enter your choice :")
    if choice2.lower()=="yes":
        continue
    elif choice2.lower()=="no":
        print("Thank you")
        break








