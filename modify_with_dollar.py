string=input("Enter the string:")
k='$'
print("Original string:",str(string))
res=string[0] + string[1:].replace(string[0],k)
print("Modified string:",str(res))
