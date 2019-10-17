class node(object):

    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

    # setter functions for the data fields
    def set_data(self,data):
        self.data=data
    
    def set_next(self,next):
        self.next=next
    
    # getter functions for the data fields

    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next



class stack(object):
    def __init__(self):
        self.head=None 

    def push(self,data):
        node1=node(data)
        if(self.head is None ):
            self.head=node1
        else:
            node1.set_next(self.head)
            self.head=node1
        
    def pop(self):
        tempNode=self.head
        self.head=self.head.get_next()
        return tempNode.get_data()

    def isEmpty(self):
        if(self.head is None):
            return True
        else:
            return False

    

