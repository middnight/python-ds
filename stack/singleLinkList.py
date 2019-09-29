from nodes import node

class singleList(object):
    #default constructor
    def __init__(self):
        self.head=None 
        self.nodeCount=0
    
    # create and insert method
    def createNode(self,data):
        node1=node(data)
        if(self.head is None):
            self.head=node1
            self.nodeCount+=1

        else:
            node1.set_next(self.head)
            self.head=node1
            self.nodeCount+=1
        
    # to delete a node from the list
    def deleteNode(self):
        if(self.head is None):
            print("stack is empty")
            return
        print("pop-up the data: ",self.head.get_data())
        self.head=self.head.get_next()
        self.nodeCount-=1

    def deleteList(self):
        self.head=None 

    def traverseList(self):
        tempNode=self.head
        if(tempNode is None):
            print("stack is empty")
            return
        while(tempNode):
            print(tempNode.get_data(),end="\t")
            tempNode=tempNode.get_next()
        print()

    def isEmpty(self):
        if(self.head is None):
            return True
        else:
            return False

