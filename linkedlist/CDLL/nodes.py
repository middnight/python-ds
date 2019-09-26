class node(object):
    # defult constructor
    def __init__(self,data=None,next=None, prev=None):
        self.data=data
        self.next=next
        self.prev=prev

    # setter methods for the data fields
    def set_data(self,data):
        self.data=data

    def set_next(self,next):
        self.next=next

    def set_prev(self,prev):
        self.prev=prev

    # getter methods for data fields
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev
