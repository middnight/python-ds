from nodes import node

# Class definition for circular single linked list
class circularList(object):
    # constructor for the class
    def __init__(self):
        self.head=None
        self.tail=None
        self.nodeCount=0

    def createList(self,data,location):
        if(self.head is None and location>0):
            print("error in circular list creation")
            return
        
        # when there is no node in list
        elif(self.head is None and location==0):
            node1=node(data)
            self.head=node1
            self.tail=node1
            node1.set_next(node1)
            self.nodeCount+=1
        
        #when we want to add at the first position
        elif( location==0):
            node1=node(data)
            node1.set_next(self.head)
            self.head=node1
            self.tail.set_next(node1)
            self.nodeCount+=1

        # when we want to add at the last node
        elif(location==self.nodeCount):
            tempNode=self.head
            node1=node(data)
            node1.set_next(self.head)
            self.tail.set_next(node1)
            self.tail=node1
            self.nodeCount+=1

        #when we want to add in between head and tail
        else:
            tempNode=self.head
            node1=node(data)
            for i in range(0,location-1):
                tempNode=tempNode.get_next()
            node1.set_next(tempNode.get_next())
            tempNode.set_next(node1)
            self.nodeCount+=1

    #to traverse in circular list
    def traverse(self):
        tempNode=self.head
        if(tempNode is None):
            print("no circular list found")
            return
        while(tempNode is not self.tail):
            print(tempNode.get_data(),end="\t")
            tempNode=tempNode.get_next()
        print(tempNode.get_data())

    # to search in a circular list
    def search(self,value):
        tempNode=self.head
        while(tempNode is not self.tail):
            if(tempNode.get_data()==value):
                print("value found in circular list: ",value)
                return
            tempNode=tempNode.get_next()
        else:
            print("value not found in circular list: ",value)


    #to delete in a circular array
    def delete(self,location):
        
        # when there is nothing to delete
        if(self.head is None):
            print("there is nothing to delete")
            return
        
        # when we want to delete the first node
        elif(location==0):
            self.head=self.head.get_next()
            self.tail.set_next(self.head)
            self.nodeCount-=1

        #when we want to delete the last node
        elif(location==self.nodeCount):
            tempNode=self.head
            for i in range(0,location-2):
                tempNode=tempNode.get_next()
            tempNode.set_next(self.head)
            self.tail=tempNode
            self.nodeCount-=1

        #when we want to delete between head and tail
        else:
            tempNode=self.head
            for i in range(0,location-1):
                tempNode=tempNode.get_next()
            tempNode.set_next(tempNode.get_next().get_next())
            self.nodeCount-=1


    #to delete the circular linked list
    def deleteList(self):
        self.head=None
        self.tail=None

    # to check linking of last node to first node 
    def check(self):
        tempNode=self.head
        for i in range(0,40):
            print(tempNode.get_data(),end="\t")
            tempNode=tempNode.get_next()
        print()





































