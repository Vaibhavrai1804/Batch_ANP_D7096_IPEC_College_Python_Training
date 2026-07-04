#creating blank list
age=[]
print("Enter ages of 10 students:")
for i in range(10):
    a=int(input())
    age.append(a)
#------------------------
print("------------------")
print("List is:")
print(age)
#Checking the eligibility
Count=0
for i in age:
    if i>=18:
        Count+=1
print("Total Number of people eligible for voting are:",Count)
