#Accept a sentence from the user and create a dictionary that stores the frequency of each word. 
sentence=input("Enter any sentence:")
update_sentence=sentence.split(" ")
list_1=[]
dict_1={}

for i in update_sentence:
    if i in list_1:
        del i
    else:
        new_count=update_sentence.count(i)
        dict_1[i]=new_count
        list_1.append(i)
        del i

print(dict_1)
#---------------------------------------------------
print("-----------------------------------------")
#Display the most frequently occurring word. 
high=0
top_word=""
for i in dict_1:
    if dict_1[i]>high:
        high=dict_1[i]
        top_word=i 
print(top_word,"Occured",high,"times which is greater amongst all the word")

#--------------------------------------------
#Display all words in alphabetical order.  
list_2=dict_1.keys
list_2.sort()
print(list_2)
