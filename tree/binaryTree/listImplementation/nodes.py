class node(object):

    def __init__(self,data=None, right=None, left=None):
        self.data=data
        self.right=right
        self.left=left

    
    def get_data(self):
        return self.data

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def set_data(self,data):
        self.data=data
    
    def set_right(self,right):
        self.right=right
    
    def set_left(self,left):
        self.left=left

class nodePointer(object):

    def __init__(self,nodePoint=None, next=None):
        self.nodePoint=nodePoint
        self.next=None 

    def set_nodePoint(self,nodePoint):
        self.nodePoint=nodePoint

    def set_next(self,next):
        self.next=next
    
    def get_nodePoint(self):
        return self.nodePoint
    
    def get_next(self):
        return self.next

class queue(object):
    def __init__(self):
        self.head=None 
        self.tail=None 
        
        self.nodeCount=0

    def enQueue(self,nodePoint):
        node1=nodePointer(nodePoint)
        if(self.head==None):
            self.head=self.tail=node1
            self.nodeCount+=1
        else:
            self.tail.set_next(node1)
            self.tail=node1
            self.nodeCount+=1

    def deQueue(self):
        tempNode=self.head
        if(self.nodeCount==1):
            self.head=self.tail=None 
            self.nodeCount-=1
            return tempNode.get_nodePoint()
        else:
            self.head=self.head.get_next()
            self.nodeCount-=1
            return tempNode.get_nodePoint()
        
    def isEmpty(self):
        if(self.head==None ):
            return True
        else:
            return False







    