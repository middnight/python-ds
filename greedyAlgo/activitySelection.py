class activity(object):
    def sort(self,arr,i):
        self.quickSort(arr,i,0,len(arr))
        #print(arr)
        return arr
    
    def quickSort(self,arr,on,start,end):
        if(start<end):
            mid=self.partition(arr,on,start,end)
            self.quickSort(arr,on,start,mid-1)
            self.quickSort(arr,on,mid+1,end)
        

    def partition(self,arr,on,start,end):
        pivot=arr[end-1][on]
        i=start
        #print(start,end,pivot)
        for j in range(start,end):
            if(arr[j][on]<=pivot):
                arr[i],arr[j]=arr[j],arr[i]
                i=i+1
        #print(arr)
        return i

    
    
    def solution(self,arr):
        act=1
        arr=self.sort(arr,1)
        previousActivity=arr[0]
        print("start time:",arr[0][0],"\t end time:",arr[0][1],"activity number",act)
        for i in range(1,len(arr)):
            if(arr[i][0]>= previousActivity[1]):
                previousActivity=arr[i]
                act+=1
                print("start time:",arr[i][0],"\t end time:",arr[i][1],"activity number",act)
        

act=activity()
arr=[[0,6],[3,4],[1,2],[5,8],[5,7],[8,9],[0,1],[9,10],[12,15]]
act.solution(arr)