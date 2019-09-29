from singleLinkList import singleList

class stack(object):
    # default constructor
    def __init__(self):
        self.link1=singleList() 
    
    # create and push 
    def push(self,data):
        self.link1.createNode(data)

    # pop-up the top of the stack
    def pop(self):
        self.link1.deleteNode()

    def isEmpty(self):
        print(self.link1.isEmpty())
    
    def deleteStack(self):
        self.link1.deleteList()

    def traverseStack(self):
        self.link1.traverseList()

        