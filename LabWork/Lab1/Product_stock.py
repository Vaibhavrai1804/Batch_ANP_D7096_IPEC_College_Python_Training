#Create a dictionary to maintain the stock of products in a shop.
dict_1={}
n=int(input("Enter number of product :"))
for i in range(n):
    print("Product",(i+1))
    pdt_name=input("Enter product name:")
    pdt_size=int(input("Enter number of given product :"))
    dict_1[pdt_name]=pdt_size

print(dict_1)
#---------------------------------------------
print("---------------------------------------")
#Add a new product.
name=input("Enter name of new product :")
size=int(input("Enter number of given product :"))
dict_1[name]=size

print("Updated dictionary",dict_1)

#-----------------------------------------------
print("---------------------------------------")
#Update the stock of an existing product. 
new_name=input("Enter product name (for which stock has to be changed) : ")
flag=False
for i in dict_1:
    if i==new_name:
        new_stock=int(input("Enter new stock :"))
        dict_1[new_name]=new_stock
        flag=True
if flag==False:
    print("No such product is available")
else:
    print("Updated dictionary",dict_1)

#Remove a product from inventory. 
remove_name=input("Enter product name (to be deleted) : ")


if remove_name in dict_1:
    del dict_1[remove_name]
    print("Updated data is:", dict_1)
else:
    print("Given product is not present in the data")
#--------------------------------------------------
print("---------------------------------------")
#Display products having stock less than 20. 
print("Products having stock less than 20. ")
for i in dict_1:
    if dict_1[i]<20:
        print(i,end=" ")


#--------------------------------------------------
print("---------------------------------------")
#Display the total number of items available in the inventory. 

count=0
list_1=dict_1.keys()
print("Total number of items available in the inventory.",len(list_1))
    

