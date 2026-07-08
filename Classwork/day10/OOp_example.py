class Rectangle:
    #memeber variable
    length=0
    beadth=0
    #method to initialize data
    def initialize(self,l,w):
        self.length=l
        self.breadth=w
    #method to display data 
    def display_data(self):
        print("------Rectangle----------")
        print("Length :",self.length,"cm")
        print("Breadth :",self.breadth,"cm")
#Object Creation
rect=Rectangle()
rect.initialize(20,50)
rect.display_data()



#-----------OUTPUT-------------
'''------Rectangle----------
Length : 20 cm
Breadth : 50 cm'''