from listImplementation import linkList

class queueList(object):
    # default constructor 

    def __init__(self):
        self.list1=linkList()

    def enQueue(self,data):
        #print("inserting",data,"in the Queue")
        self.list1.createNode(data)

    def deQueue(self):
        self.list1.deleteNode()

    def isEmpty(self):
        if(self.list1.isEmpty()):
            print("Queue is empty")
        else:
            print("Queue is not empty")

    def deleteQueue(self):
        if(self.list1.isEmpty()):
            print("Queue is empty")
        else:
            print("deleting the Queue now")
            self.list1.deleteList()

    def printQueue(self):
        if(self.list1.isEmpty()):
            print("Queue is empty")
        else:
            self.list1.traverse()





    