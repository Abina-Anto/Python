list=[]
name=input("Enter the first name :")
list.append(name)
count=0
for i in list[0]:
    if i=='a':
        count=count+1
print("Count of a in",list[0],":",str(count))
    
