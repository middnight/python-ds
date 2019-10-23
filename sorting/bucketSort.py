import quickSort
import math

# in bukcetsort we divide the given array into number of buckets and 
# sort them independetly and combine them
def bucketSort(array,maxValue):
    noOfBuckets=int(math.floor(math.sqrt(len(array))))
    print(noOfBuckets)
    buckets=list()
    for i in range(noOfBuckets):
        buckets.append(list())
    for i in array:
        appropriateBucket=int(math.ceil((i*noOfBuckets)/maxValue))
        #print(i,appropriateBucket,end="\t")
        buckets[appropriateBucket-1].append(i)
    print()
    #print(buckets)
    # sorting the individual buckets independently using quick sort O(n)=nlog n 
    for i in buckets:
        quickSort.sort(i)
    #print(buckets)
    sortedList=[]
    for i in buckets:
        for j in i:
            sortedList.append(j)

    print(sortedList)


list1=[90,85,75,80,65,55,45,32,12,10,9,425,35,35,234,45,243]
bucketSort(list1,425)