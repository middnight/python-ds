def sort(arr):
        quickSort(arr,0,len(arr)-1)
        #print("1",list1)
        #print(arr)
        return arr
    
def quickSort(arr,start,end):
    if(start<=end):
        mid=partition(arr,start,end)
        quickSort(arr,start,mid-1)
        quickSort(arr,mid+1,end)

def partition(arr,start,end):
    pivot=arr[end]
    i=start-1
    #print(start,end,pivot)
    for j in range(start,end+1):
        if(arr[j]<=pivot):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    #print(arr)
    return i

#list1=[23,4,45,24,6,46,7,3,8,5,9,547,3,4,43,78,4,5,9,4,5,9,325,36,8,2,35,8,46,734,52,453]
#print(list1)
#list1=[2000,500,200,100,50,20,10,5,2,1]
#print(sort(list1))