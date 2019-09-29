class node(object):
    # default constructor for the class

    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

    # getter methods for the data fields

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    # setter methods for the data fields

    def set_data(self,data):
        self.data=data
    
    def set_next(self,next):
        self.next=next
        