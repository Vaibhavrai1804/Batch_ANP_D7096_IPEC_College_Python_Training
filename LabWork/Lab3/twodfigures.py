#Module that contains functions to perform the following calculations for different two-dimensional shapes: 

#Shape 1 :Triangle
#Choice : Area

def trainglearea(a,b,c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        s = (a+b+c) / 2
        area = (s * (s - a) * (s - b) * (s - c))**0.5
        return area 
    else:
        return "Invalid traingle"
    
#Choice : Perimeter
def traingleperimeter(a,b,c):
    return (a+b+c)

#----------------------------------

#Shape 2 :Circle
#Choice : Area

def circlearea(radius):
    return (3.14*(radius**2))

#Choice : Perimeter
def circleperimeter(radius):
    return (2*3.14*radius)

#----------------------------------

#Shape 3 :Square
#Choice : Area

def squarearea(side):
    return (side*side)

#Choice : Perimeter
def squareperimeter(side):
    return (4*side)

#----------------------------------

#Shape 4 :Rectangle
#Choice : Area

def rectanglearea(a,b):
    return (a*b)

#Choice : Perimeter
def rectangleperimeter(a,b):
    return (2*(a+b))




    


   



