num=10
f1=0
f2=1
print(f1,end=" ")
print(f2,end=" ")
for i in range(2,num+1):
    f3 =f1+f2
    f1=f2
    f2=f3
    print(f3,end=" ")
