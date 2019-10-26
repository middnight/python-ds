"""
problem statement:
1. there are n number of houses build in a line each of them contains some value in them
2. a thief is going to steal maximum values from there houses
3. but he can't steal from two adajcent houses
4. what is the maximum value he can steal




"""

def houseThief(array, currentIndex):
    if(currentIndex > len(array)-1):
        return 0
    else:
        # when he staels from the current house, he mush not steal from next house so 
        # currentIndex+=2
        count1=array[currentIndex]+ houseThief(array,currentIndex+2)
        # when he does not steal from current index house then
        # currentIndez+=1
        count2= 0+houseThief(array,currentIndex+1)
        return max(count1,count2)

list1=[6,7,1,30,8,2,4,87,0,97,75,54,9,75]
print(houseThief(list1,0))