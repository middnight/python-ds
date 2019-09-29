from nodes import node

class linkList(object):

    #default constructor for the class
    def __init__(self):
        self.head=None 
        self.tail=None 
        self.nodeCount=0
    
    def createNode(self,data):
        node1=node(data)
        if(self.head is None):
            self.head=node1
            self.tail=node1
            self.nodeCount+=1
        else:
            self.tail.set_next(node1)
            self.tail=node1
            self.nodeCount+=1

    def deleteNode(self):
        if(self.isEmpty()):
            print("Queue is already empty")
            return
        tempNode=self.head
        self.head=self.head.get_next()
        self.nodeCount-=1
        print(tempNode.get_data())
        tempNode=NotImplemented

    def peek(self):
        if(self.isEmpty()):
            print("Queue is empty")
            return

        print(self.head.get_data())

    def isEmpty(self):
        if(self.head is None):
            return True
        else:
            return False
    
    def deleteList(self):
        self.head=None 
        self.tail=None    

    def traverse(self):
        tempNode=self.head
        while(tempNode):
            print(tempNode.get_data(),end="\t")
            tempNode=tempNode.get_next()
        print()

