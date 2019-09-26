class node(object):
    # constructor for the class
    def __init__(self,data=None, next=None):
        self.data=data
        self.next=next
    
    # get method for data pf node
    def get_data(self):
        return self.data

    #get method for reference to the next node
    def get_next(self):
        return self.next
    
    #set method for node's data property
    def set_data(self,data):
        self.data=data

    #set method for node's reference property
    def set_next(self,next):
        self.next=next

    
    



