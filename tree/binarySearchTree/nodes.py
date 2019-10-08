class node(object):

    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
    
    # getter methods for the data fields

    def get_data(self):
        return self.data
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right

    #setter methods for the data field
    def set_data(self,data):
        self.data=data  

    def set_left(self,left):
        self.left=left
    
    def set_right(self,right):
        self.right=right 

