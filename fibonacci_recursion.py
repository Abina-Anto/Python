def fibonacci(n):
    if(n<=1):
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
n=int(input("Enter the number of terms:"))
if n<=0:
    print("Please enter a positive number:")
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(fibonacci(i))
    
