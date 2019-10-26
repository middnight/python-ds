def knapsack(arrofWeight,arrOfProfit,capacity,currentIndex):
    if(currentIndex>len(arrofWeight)-1 or capacity<=0 or currentIndex<0):
        return 0
    list1=[]
    if(arrofWeight[currentIndex]<= capacity):
        profit1=arrOfProfit[currentIndex]+ knapsack(arrofWeight,arrOfProfit,capacity-arrofWeight[currentIndex], currentIndex+1)
        list1.append(profit1)
    profit2=knapsack(arrofWeight,arrOfProfit,capacity,currentIndex+1)
    list1.append(profit2)
    return max(list1)







profit=[31,26,72,17]
weights=[3,1,5,2]
print(knapsack(weights,profit,7,0))