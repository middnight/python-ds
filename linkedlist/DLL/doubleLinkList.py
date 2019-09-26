from nodes import node

class doubleLinkList(object):
    # default contructor for the class
    def __init__(self):
        self.head=None
        self.tail=None
        self.nodeCount=0

    def createList(self,data,location):
        node1=node(data)
        if(self.head==None and location==0):
            self.head=node1
            self.tail=node1
            self.nodeCount+=1
        
        elif(location ==0):
            node1.set_next(self.head)
            self.head.set_prev(node1)
            self.head=node1
            self.nodeCount+=1

        elif(location>=self.nodeCount):
            node1.set_prev(self.tail)
            self.tail.set_next(node1)
            self.tail=node1
            self.nodeCount+=1

        else:
            tempNode=self.head
            for i in range(0,location-1):
                tempNode=(tempNode.get_next())
            node1.set_next(tempNode.get_next())
            node1.set_prev(tempNode)
            tempNode.set_next(node1)
            node1.get_next().set_prev(node1)
            self.nodeCount+=1
    # for forward traversing the linked list
    def traverse(self):
        tempNode=self.head
        if(tempNode is None):
            print("no linked list found to traverse")
            return
        
        while(tempNode):
            print(tempNode.get_data(),end="\t")
            tempNode=tempNode.get_next()
            
        print()

    #for reverse traversing the linked list
    def reverseTraverse(self):
        tempNode=self.tail
        if(tempNode is None):
            print(" no linked list found to reverse traverse")
            return
        while(tempNode):
            print(tempNode.get_data(),end="\t")
            tempNode=tempNode.get_prev()
        print()

    # for searching an value in the linked list
    def search(self, value):
        tempNode=self.head
        while(tempNode):
            if(tempNode.get_data()==value):
                print("value is found: ",value)
                return
            tempNode=tempNode.get_next()
        print("value not found: ",value)
        return 

    # to delete a node from the list
    def deleteNode(self,location):
        if(self.head is None):
            print(" no linked list found")
            return
        # want to delete the first node in the list and if it's the only node in the list
        elif(location==0 and self.nodeCount==1):
            self.head=None
            self.tail=None 
            self.nodeCount-=1
        # want to delete first node in the list
        elif(location ==0 ):
            self.head=self.head.get_next()
            self.head.set_prev(None)
            self.nodeCount-=1
        # want to delete the last node in the list
        elif(location==self.nodeCount):
            self.tail=self.tail.get_prev()
            self.tail.set_next(None)
            self.nodeCount-=1
        # want to delete any node in between
        else:
            tempNode=self.head
            for i in range(0,location-1):
                tempNode=tempNode.get_next()
            tempNode.set_next(tempNode.get_next().get_next())
            tempNode.get_next().set_prev(tempNode)
            self.nodeCount-=1
        
    # to delete the entire double linked list
    def deleteList(self):
        if(self.head is None):
            print("no linked list found")
            return
        else:
            tempNode=self.head
            for i in range(0,self.nodeCount):
                tempNode.set_prev(None)
                tempNode=tempNode.get_next()
            self.nodeCount=0
            self.head=None 
            self.tail=None 

        


























