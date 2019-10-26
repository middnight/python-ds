"""
fibonacci series is a series of numbers in which each number is sum of last two numbers.
first two numbers by default are 0 and 1.
"""

def fibonacci(N):
    if(N<0):
        return None
    elif(N==1):
        return 0
    elif(N==2):
        return 1
    elif(N>2):
        return fibonacci(N-1)+ fibonacci(N-2) 

print(fibonacci(20))