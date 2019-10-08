from nodes import node 
from nodes import queue
from nodes import nodePointer

class binaryTree(object):
    def __init__(self):
        self.root=None 
        self.nodeCount=0

    def insertNode(self,data):
        node1=node(data)
        if(self.root==None ):
            self.root=node1 
            self.nodeCount+=1
        else:
            node1=node(data)
            q1=queue()
            q1.enQueue(self.root)
            while(not (q1.isEmpty())):
                tempNode=q1.deQueue()
                if(tempNode.get_left() is not None ):
                    q1.enQueue(tempNode.get_left())
                elif(tempNode.get_left() is None):
                    tempNode.set_left(node1)
                    self.nodeCount+=1
                    print(data,"added to tree at position",self.nodeCount)
                    return 
                elif(tempNode.get_right() is not None ):
                    q1.enQueue(tempNode.get_right())
                elif(tempNode.get_right() is None ):
                    tempNode.set_right(node1)
                    self.nodeCount+=1
                    print(data,"added to tree at position",self.nodeCount)
                    return 
                


    def traversal(self):
        if(self.root is None ):
            print(" NO tree found to traverse")
            return
        q1=queue()
        q1.enQueue(self.root)
        while(not q1.isEmpty()):
            tempNode=q1.deQueue()
            print(tempNode.get_data(),end="\t")
            if(tempNode.get_left() is not None ):
                q1.enQueue(tempNode.get_left())
            elif(tempNode.get_right() is not None ):
                q1.enQueue(tempNode.get_right())
            else:
                print()
                return
        

    def isEmpty(self):
        if(self.root==None ):
            return True
        else:
            return False


    def deleteNode(self,data):
        if(self.root is None or (self.root.get_left() is None  and self.root.get_right() is None)):
            self.root=None 
            print("root deleted")
        else:
            lastNode=self.root
            foundNode=None
            q1=queue()
            q1.enQueue(self.root)
            while(not q1.isEmpty()):
                tempNode=q1.deQueue()
                if(tempNode.get_data() == data):
                    foundNode=tempNode
                if(tempNode.get_left() is not None ):
                    q1.enQueue(tempNode.get_left())
                elif(tempNode.get_right() is not None):
                    q1.enQueue(tempNode.get_right())
                else:
                    foundNode.set_data(tempNode.get_data())
                    if(lastNode.get_left() == tempNode):
                        lastNode.set_left(None)
                        return
                    elif(lastNode.get_right() ==tempNode):
                        lastNode.set_right(None)
                        return
                lastNode=tempNode
            print("node with data",data," not found")
        
    def search(self,data):
        if(self.root is None ):
            print("no tree found to search")
            return
        q1=queue()
        q1.enQueue(self.root)
        while(not q1.isEmpty()):
            tempNode=q1.deQueue()
            if(tempNode.get_data() == data):
                print("value forund in tree",data)
                return
            elif(tempNode.get_left() is not None ):
                q1.enQueue(tempNode.get_left())
            elif(tempNode.get_right() is not None):
                q1.enQueue(tempNode.get_right())
        print("value not found in tree",data)