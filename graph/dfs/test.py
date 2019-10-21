def solution(N):
    list1=[i for i in range(1,N+1)]
    list2=recurse(0,list1)
    #print(list2)


def recurse(start,list1):
    if(len(list1)==2):
        print(list1)
        return 
    else:
        if(start<= len(list1)-3):
            list1.pop(start+2)
            #print("condtion1",list1.pop(start+2))
        elif(start==len(list1)-2):
            list1.pop(0)
            #print("condtion2",list1.pop(0))
        elif(start==len(list1)-1):
            list1.pop(1)
            #print("condtion3",list1.pop(1))
        elif(start==len(list1)):
            list1.pop(1)
            #print("condtion3",list1.pop(1))
        else:
            start=-1
        recurse(start+1,list1)



solution(16)