import sys

def Factorial(n): 
    result = 1
    for i in range (1,n):
        result = result * i
    
    return result

print Factorial(6)
