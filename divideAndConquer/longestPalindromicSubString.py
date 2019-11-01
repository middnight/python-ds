"""
problem statement-
1. we wre given a string s.
2. we need to find the length of longest palindromic sub string.

substring- a substring is a contagious sequence of characters with in a string.

"""

def calculate(str1,startIndex,endIndex):
    list1=[]
    if(startIndex>endIndex):
        return 0
    if(startIndex==endIndex):
        return 1
    if(str1[startIndex]==str1[endIndex]):
        remainLength=endIndex-startIndex-1
        if(remainLength==calculate(str1,startIndex+1,endIndex-1)):
            list1.append(remainLength+2)
    list1.append(calculate(str1,startIndex+1,endIndex))
    list1.append(calculate(str1,startIndex,endIndex-1))
    return max(list1)



str1='abccbuaub'
print(calculate(str1,0,len(str1)-1))