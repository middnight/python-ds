"""
problem statement:
given N, count number of ways to express N as the sum of 1,3,4
we can use the same number multiple times

if(n==0 or n==1 or n==2)
then no of ways=1
ex: 0 - {}, 1- {1}, 2-{1,1}
if(n==3)
the no of ways=2
ex: 3 - {1,1,1}, {3}


"""

def numberFactor(N):
    if(N==0 or N==1 or N==2):
        return 1
    elif(N==3):
        return 2
    c1=numberFactor(N-1)
    c2=numberFactor(N-3)
    c3=numberFactor(N-4)
    
    return c1+c2+c3



print(numberFactor(4))