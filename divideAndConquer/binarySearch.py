import quickSort

def binarySearch(array,start,end,value):
    arr=quickSort.sort(array)
    mid=(start+end)//2
    if(start>end):
        return

    elif(arr[mid]<value):
        return binarySearch(arr,mid+1,end,value)
    elif(arr[mid]>value):
        return binarySearch(arr,start,mid,value)
    elif(arr[mid]==value):
        print("value found at index:",mid)
        return 


list1=[23,4,45,24,6,46,7,3,8,5,9,547,3,4,43,78,4,5,9,4,5,9,325,36,8,2,35,8,46,734,52,453]
#print(list1)
#print(quickSort.sort(list1),list1.index(453))
binarySearch(list1,0,len(list1),734)
