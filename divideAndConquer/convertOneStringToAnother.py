def calculateMinimumOperation(str1,str2,index1,index2):
    if(len(str1)-1==index1):
        return len(str2)-1-index2
    if(len(str2)-1==index2):
        return len(str1)-1-index1
    if(str1[index1]==str2[index2]):
        return calculateMinimumOperation(str1,str2,index1+1,index2+1)
    count1=1+calculateMinimumOperation(str1,str2,index1+1,index2)
    count2=1+calculateMinimumOperation(str1,str2,index1,index2+1)
    count3=1+calculateMinimumOperation(str1,str2,index1+1,index2+1)
    return min(count1,count2,count3)






str1="table"
str2="tgcable"

print(calculateMinimumOperation(str1,str2,0,0))
