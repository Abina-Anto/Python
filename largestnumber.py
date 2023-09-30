a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a>b and a>c:
    print(a,"is largest")
elif b>a and b>c:
    print(b,"is largest")
elif c>a and c>b:
    print(c,"is largest")
else:
    print("numbers are equal")
