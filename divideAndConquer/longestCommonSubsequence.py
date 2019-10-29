"""
problem statement-
1. we are given two strings s1 and s2.
2. we need to find the length og the longest subsequence which is common in both the strings.

"""

def calculate(str1,str2,currIndex1,currIndex2):
    list1=[]
    if(currIndex1>len(str1)-1 or currIndex2>len(str2)-1):
        return 0
    if(str1[currIndex1]==str2[currIndex2]):
        c1=0
        c1=1+ calculate(str1,str2,currIndex1+1,currIndex2+1)
        list1.append(c1)
    else:
        c2=calculate(str1,str2,currIndex1,currIndex2+1)
        c3=calculate(str1,str2,currIndex1+1,currIndex2)
        list1.append(c2)
        list1.append(c3)
    return max(list1)

str1='elephant'
str2='eretpat'
print(calculate(str1,str2,0,0))

str1='roronoaZoro'
str2='zorosan'
print(calculate(str1,str2,0,0))