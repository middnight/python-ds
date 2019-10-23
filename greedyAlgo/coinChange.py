
class coinChange(object):
    def getMinimumCoins(self,arrayOfCoins,amount):
        arr=arrayOfCoins
        arr.sort()
        temp=amount
        arr=arr[::-1]
        count=0
        i=0
        print(arr)
        while(True):
            if(i<=len(arr)-1 and arr[i]<=amount ):
                amount=amount-arr[i]
                count+=1
                print(arr[i],end="\t")
                i=0
            else:
                i+=1
            if(amount==0):
                break
        print("\nnumber of minimum coins needed are :",count," for the amount of:",temp)



c1=coinChange()
listOfCoins=[2000,500,200,100,50,20,10,5,2,1]
c1.getMinimumCoins(listOfCoins,2738)
