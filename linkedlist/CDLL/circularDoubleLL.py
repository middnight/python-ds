from nodes import node

class circularDoubleLL(object):
    # default constructor
    def __init__(self):
        self.head=None
        self.tail=None
        self.nodeCount=0

    # creation and insertion in a linked list
    def createList(self,value,location):
        node1=node(value)
        if(self.head==None and location>0):
            print("no link list found to add the node at given location")
        
        #when there is no node in the list
        elif(self.head== None and location==0):
            self.head=node1
            self.tail=node1
            node1.set_next(node1)
            node1.set_prev(node1)
            self.nodeCount+=1
            
        # when we want to add a node in 0th position
        elif(location==0):
            node1.set_next(self.head)
            node1.set_prev(self.tail)
            self.head.set_prev(node1)
            self.tail.set_next(node1)
            self.nodeCount+=1
        
        #when we want to add at last position
        elif(location>=self.nodeCount):
            node1.set_prev(self.tail)
            self.tail.set_next(node1)
            self.head.set_prev(node1)
            node1.set_next(self.head)
            self.tail=node1
            self.nodeCount+=1
        
        #when we want to add node in between 
        else:
            tempNode=self.head
            for i in range(0,location-1):
                tempNode=tempNode.get_next()
            node1.set_next(tempNode.get_next())
            node1.set_prev(tempNode)
            tempNode.set_next(node1)
            node1.get_next().set_prev(node1)
            self.nodeCount+=1
        
    def traverse(self):
        tempNode=self.head
        if(tempNode is None):
            print(" no linked list found to traverse")
            return
        while(tempNode is not self.tail):
            print(tempNode.get_data(),end="\t")
            tempNode=tempNode.get_next()
        print(tempNode.get_data())
    
    def reverseTraverse(self):
        tempNode=self.tail
        if(tempNode is None):
            print("no linked list found to traverse")
            return
        while(tempNode is not self.head):
            print(tempNode.get_data(),end="\t")
            tempNode=tempNode.get_prev()
        print(tempNode.get_data())

    def test(self):
        tempNode=self.head
        if(tempNode is None):
            print("no linked list found to test")
            return
        for i in range(0,50):
            print(tempNode.get_data(),end="\t")
            tempNode=tempNode.get_next()
        print()

    def revTest(self):
        tempNode=self.tail
        if(tempNode is None):
            print("no linked list found to test")
            return
        for i in range(0,50):
            print(tempNode.get_data(),end="\t")
            tempNode=tempNode.get_prev()
        print()


        
    def search(self,value):
        tempNode=self.head
        for i in range(0,self.nodeCount):
            if(tempNode.get_data()==value):
                print("value is found :",value)
                return
            tempNode=tempNode.get_next()
        else:
            print("value not found :",value)
            return

    def deleteNode(self,location):
        if(self.head==None):
            print("no linked list found to delelte nodes")
            return
        
        #we want to delete the first node and it is only node in the list
        elif(location==0 and self.nodeCount==1):
            self.head.set_next(None)
            self.head.set_prev(None)
            self.Head=None 
            self.tail=None 
            self.nodeCount-=1

        # we want to delete the first node in the list
        elif(location==0):
            print("hi")
            self.head=(self.head.get_next())
            self.head.set_prev(self.tail)
            self.tail.set_next(self.head)
            self.nodeCount-=1

        # we want to delete the last node in the list
        elif(location==self.nodeCount):
            self.tail=self.tail.get_prev()
            self.tail.set_next(self.head)
            self.head.set_prev(self.tail)
            self.nodeCount-=1

        # we want to delete in between nodes
        else:
            tempNode=self.head
            for i in range(0,location-1):
                tempNode=tempNode.get_next()
            tempNode.set_next(tempNode.get_next().get_next())
            tempNode.get_next().set_prev(tempNode)
            self.nodeCount-=1

    # we want to delete the entire linked list
    def deleteList(self):
        tempNode=self.head
        for i in range(0,self.nodeCount):
            tempNode.set_prev(None)
            tempNode=tempNode.get_next()
        self.head=None 
        self.tail=None
        self.nodeCount=0 









            
