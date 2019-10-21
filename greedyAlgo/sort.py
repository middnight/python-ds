def sort(arr):
        quickSort(arr,0,len(arr))
        #print("1",list1)
        print(arr)
        
    
def quickSort(arr,start,end):
    if(start<end):
        mid=partition(arr,start,end)
        quickSort(arr,start,mid-1)
        quickSort(arr,mid+1,end)

def partition(arr,start,end):
    pivot=arr[end-1]
    i=start-1
    print(start,end,pivot)
    for j in range(start,end):
        if(arr[j]<=pivot):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    print(arr)
    return i


list1=[3,6,1,2,8,9,12,3,4]
sort(list1)