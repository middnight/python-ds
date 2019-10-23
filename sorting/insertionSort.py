def insertionSort(array):
    for i in range(1,len(array)):
        currentIndex=i
        for j in range(0,i):
            if(array[j]> array[currentIndex]):
                array[j],array[currentIndex]=array[currentIndex],array[j]
    print(array)


list1=[200,34,546,235,58,35,798,235,98,436,9,235,9,43,23,434,8,25]
insertionSort(list1)