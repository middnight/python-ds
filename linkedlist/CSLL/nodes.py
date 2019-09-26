class node(object):
    # constructor of node class
    def __init__(self, data=None,next=None):
        self.data=data
        self.next=next
    
    # setter method for data
    def set_data(self,data):
        self.data=data
    
    #setter method for next reference
    def set_next(self,next):
        self.next=next

    #getter method for data
    def get_data(self):
        return self.data
    
    #getter method for next reference
    def get_next(self):
        return self.next

        