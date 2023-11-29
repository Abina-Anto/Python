f=input("Enter the filename:")
try:
    fileptr=open(f,"r")
    data=fileptr.read()
    print(data)
    try:
        fileptr=open("file.txt","w")
        fileptr.write("welcome")
    finally:
        fileptr.close()
        print("file closed")
except:
    print("Error") 
