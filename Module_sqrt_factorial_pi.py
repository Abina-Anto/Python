def factorial(x):
     if x == 1:
            return 1
     else:
        return (x * factorial(x-1))
import math
n=float(input("Enter the number = "))
result = factorial(n)
print("The factorial is", result)
print("Square Root",math.sqrt(n))
print("pi",math.pi)
