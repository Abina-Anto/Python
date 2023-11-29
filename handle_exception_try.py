f=input("Enter the filename:")
try:
    f2=open(f,"r")
    data=f2.read()
    print(data)
except:
    print ("No file named",f)
