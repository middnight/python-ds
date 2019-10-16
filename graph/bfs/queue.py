# node implementation for the linked list

class node(object):
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

    # getter functions for the data field
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    # setter functions for the data fields

    def set_data(self,data):
        self.data=data
    
    def set_next(self,next):
        self.next=next

# single linked list implemetation for the purpose of adjcaency list

class queue(object):

    def __init__(self):
        self.head=None 
        self.tail=None 
        #self.nodeCount=0

    def enQueue(self,vertex):
        node1=node(vertex)
        if(self.head==None ):
            self.head=self.tail=node1
        else:
            self.tail.set_next(node1)
            self.tail=node1

    def deQueue(self):
        tempNode=self.head
        self.head=self.head.get_next()
        return tempNode.get_data()

    def isEmpty(self):
        if(self.head is None):
            return True
        else:
            return False
            


            


