def selectionSort(array):
    for i in range(len(array)):
        minimum=i
        for j in range(i,len(array)):
            if(array[j]< array[minimum]):
                minimum=j
        if(minimum != i):
            array[i],array[minimum]=array[minimum],array[i]
    print(array)


list1=[2000,500,200,100,50,20,10,5,2,1]
selectionSort(list1)