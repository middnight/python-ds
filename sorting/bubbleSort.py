def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if(array[j]>array[j+1]):
                array[j],array[j+1]=array[j+1],array[j]
    print(array)


list1=[2000,500,200,100,50,20,10,5,2,1]
bubbleSort(list1)