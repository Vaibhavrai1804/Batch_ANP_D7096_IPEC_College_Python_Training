#Create a blank list
number=[]
print("Enter 20 number:")
for i in range(20):
    a=int(input())
    number.append(a)
print("List is:",number)
#--------------------------
print("-----------------------")
number.sort()
print("3rd largest number is:",number[-3])
