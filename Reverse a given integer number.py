num =int(input("Enter the number:"))
temp= 0
while num!=0:
    digit=num%10
    temp=temp*10+digit
    num=num//10

print("Reversed Number:"+str(temp))
