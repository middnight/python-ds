from nodes import node

class binarySeacrhTree(object):
    def __init__(self):
        self.root=None
        self.nodeCount=0
        self.list1=[]



    def insertInBst(self,currentNode,value):
        if(currentNode is None ):
            currentNode=node(value)
            self.nodeCount+=1
            
        elif(value < currentNode.data):
            currentNode.set_left(self.insertInBst(currentNode.get_left(),value))
        else:
            currentNode.set_right(self.insertInBst(currentNode.get_right(),value))
        return currentNode

    def insert(self,value):
        if(self.root is None ):
            node1=node(value)
            self.root=node1
            self.nodeCount+=1
            return
        else:
            self.insertInBst(self.root,value)
            return

    def traverseIn(self, root):
        #print("we are using in order traversal here")
        if(root is None):
            return 
        else:
            
            self.traverseIn(root.get_left())
            print(root.get_data(),end="\t")
            self.traverseIn(root.get_right())
            
    def inOrder(self,root):
        if(root is None ):
            return
        else:
            self.inOrder(root.get_left())
            self.list1.append(root.get_data())
            self.inOrder(root.get_right())
    def search(self,root,value):
        if(root is None ):
            return None 
        elif(value < root.get_data() ):
            return self.search(root.get_left(),value)
        elif(value > root.get_data()):
            return self.search(root.get_right(), value)
        else:
            return root



    def delete(self,value):
        if(self.root is None ):
            print("no tree found")
            return 
        else:
            print("deleteNode called")
            self.deleteNode(self.root, value)

    def deleteNode(self,root,value):
        if(root is None):
            return None 
        elif(value < root.get_data()):
            root.set_left(self.deleteNode(root.get_left(),value))
            return root
        elif(value > root.get_data()):
            root.set_right(self.deleteNode(root.get_right(),value))
            return root
        else:
            if((root.get_left() is None) and (root.get_right() is None )):
                root=None
                return root
            elif((root.get_left() is not None) and (root.get_right() is not None )):
                self.inOrder(self.root)
                temp=self.list1.index(root.get_data())
                successor=self.list1[temp+1]
                print("successor:",successor)
                #tempNode=self.search(self.root,successor)
                self.deleteNode(self.root,successor)
                root.set_data(successor)
                return root
            elif( (root.get_left() is not None ) or ( root.get_right()is not None)):
                if(root.get_left() is not None):
                    root=root.get_left()
                else:
                    root=root.get_right()
                
                return root




                

