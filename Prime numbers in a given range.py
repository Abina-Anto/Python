l=int(input("Enter the lower bound:"))
u=int(input("Enter the upper bound:"))
for num in range(l,u+1):
    if(num>1):
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num)
    
