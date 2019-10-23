class knapSack(object):
    
    def sort(self,array,on,startIndex,endIndex):
        if(startIndex<=endIndex):
            mid=self.partion(array,on,startIndex,endIndex)
            #print(mid)
            #print(array)
            self.sort(array,on,startIndex,mid-1)
            self.sort(array,on,mid+1,endIndex)
        else:
            return array

    
    def partion(self,array,on,startIndex,endIndex):
        pivot=array[endIndex][on]
        #print(pivot)
        i=startIndex-1
        for j in range(startIndex,endIndex+1):
            if(array[j][on]>= pivot):
                i+=1
                array[i],array[j]=array[j],array[i]
        return i

    
    
    def calcuateMaxProfit(self,array,weight):
        calculatedArray=[]
        profit=0
        # adding a third column for density of the elements, density= value/weight
        for i in array:
            density=i[1]/i[0]
            temp=[i[0],i[1],density]
            calculatedArray.append(temp)
        #print(calculatedArray)
        # sorthing the rows in decreasing order of density
        self.sort(calculatedArray,2,0,len(calculatedArray)-1)
        #print(calculatedArray)
        for i in calculatedArray:
            if(weight==0):
                break
            elif(i[0]<= weight and weight >0):
                weight-=i[0]
                profit+=i[1]
                print("taken :",i[0],"weight of density:",i[2])
            else:
                if(i[0]> weight and weight>0):
                    print("taken :",weight," of density:",i[2])
                    profit+=weight*i[2]
                    weight-=weight
        print("maximum profit is :",profit)




k=knapSack()
array=[[6,6],[10,2],[3,1],[5,8],[1,3],[3,5]]
k.calcuateMaxProfit(array,10)