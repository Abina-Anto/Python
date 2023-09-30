a=int(input("Enter first number"))
b=int(input("Enter second number"))
print("\n1.Addition\n2.Substraction\n3.Multiplication\n4.Division")
ch=int(input("Enter the choice"))
if(ch==1):
    c=a+b
    print("sum=",c)
elif(ch==2):
    c=a-b
    print("Substraction=",c)
elif(ch==3):
    c=a*b
    print("Multiplication=",c)
elif(ch==4):
    c=a/b
    print("Division=",c)
else:
    print("Error choice")
