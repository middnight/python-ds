# this is implementation for a  min heap
class binaryHeap(object):
    
    def __init__(self):
        self.array=[None]
        self.lastUsedIndex=0

    def insert(self, value):
        self.array.append(value)
        self.lastUsedIndex+=1
        self.checkHeapFromBottom(self.lastUsedIndex)
    

    def sizeOfHeap(self):
        return self.lastUsedIndex
    
    def peekOfHeap(self):
        return self.array[1]

    def compare(self,index1,index2):
        if(self.lastUsedIndex< index2 and self.lastUsedIndex< index1):
            return 0
        elif (self.lastUsedIndex< index2):
            return index1
        elif(self.array[index1]< self.array[index2]):
            return index1
        else:
            return index2


    def extract(self):
        self.array[1]=self.array[self.lastUsedIndex]
        del self.array[self.lastUsedIndex]
        self.lastUsedIndex-=1
        self.checkHeapFromTop(1)
    
    def checkHeapFromBottom(self, index):
        if(index <=1):
            return
        temp=index
        parentTemp=(temp//2)
        if(self.array[parentTemp]> self.array[temp]):
            self.array[parentTemp],self.array[temp]=self.array[temp], self.array[parentTemp]
        self.checkHeapFromBottom(parentTemp)

    def checkHeapFromTop(self,index):
        if(index>=self.lastUsedIndex):
            return
        temp=self.compare(2*index, 2*index+1)
        if(temp==0):
            return
        if(self.array[index]>self.array[temp]):
            self.array[index],self.array[temp]=self.array[temp], self.array[index]
        index=temp
        self.checkHeapFromTop(index)

    def traverse(self):
        for i in range(1,self.lastUsedIndex+1):
            print(self.array[i],end="\t")
        print()




