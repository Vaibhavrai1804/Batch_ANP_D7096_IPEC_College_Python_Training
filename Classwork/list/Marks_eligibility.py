#Creating blank list
names=[]
marks=[]
print("Enter names and marks of 15 students:")
for i in range(15):
    name=input()
    mark=int(input())
    names.append(name)
    marks.append(mark)
#-----------------------
print("--------------------")
#checking the eligibility
print("Names of student who are eligible ")
for i in range(15):
    if marks[i]>75:
        print(names[i])
   
