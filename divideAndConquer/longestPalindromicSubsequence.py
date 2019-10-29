"""
problem statement-
1. we are given a string s.
2. we need to find the length of it's longest palindromic subsequence.
3. a palindrom is a string that reads the same backward as well as forward and can be odd or even length.


"""

def calculate(str1,startIndex,endIndex):
    list1=[]
    if(startIndex> endIndex):
        return 0
    if(startIndex==endIndex):
        return 1
    if(str1[startIndex]==str1[endIndex]):
        list1.append(2+calculate(str1,startIndex+1,endIndex-1))
    # if they don't match we can have two operations
    list1.append(calculate(str1,startIndex+1,endIndex))
    list1.append(calculate(str1,startIndex,endIndex-1))
    return max(list1)


str1='elrmenmet'
print(calculate(str1,0,len(str1)-1))