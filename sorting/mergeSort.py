def mergeSort(array):
    start=0
    end=len(array)
    if(end>1):
        mid=(start+end)//2
        arr1=array[start:mid]
        arr2=array[mid:end]
        
        list1=mergeSort(arr1)
        list2=mergeSort(arr2)
        list3=merge(list1,list2)
        
        return list3
    else:
        return array
def merge(arr1,arr2):
    
    mergeList=[]
    while(arr1 and arr2):
        if(arr1[0]< arr2[0]):
            mergeList.append(arr1[0])
            arr1.pop(0)
        else:
            mergeList.append(arr2[0])
            arr2.pop(0)
    if(arr1):        
        mergeList+=arr1
    if(arr2):
        mergeList+=arr2
    
    return mergeList






list1=[2000,500,200,45,100,23,50,20,10,5,2,1]
print(mergeSort(list1))