from nodes import node

class linklist(object):

    #constructor for the class linked list
    def __init__(self):
        self.head=None
        self.tail=None
        self.nodeCount=0
    
    # method to create a linked list
    def createList(self,data,location):
        #when there is no linked list and we want to add at a given position
        if(self.head is None and location>0):
            return ("there is no link list")
        
        # when there is no node in the linked list
        if(self.head is None and location==0):
            node1= node(data)
            self.head=node1
            self.tail=node1
            self.nodeCount+=1
        #when we want to add at the starting of the list
        elif(location==0):
            node1=node(data)
            node1.set_next(self.head)
            self.head=node1
            self.nodeCount+=1

        #when we want to add a node at the last position
        elif(location==self.nodeCount and location >0):
            node1=node(data)
            self.tail.set_next(node1)
            self.tail=node1
            self.nodeCount+=1
        #when we want to add a node in between head and tail
        else:
            node1=node(data)
            tempNode=self.head
            for i in range(0,location-1):
                tempNode=tempNode.get_next()
            node1.set_next(tempNode.get_next())
            tempNode.set_next(node1)
            self.nodeCount+=1

    #method to traverse a given linked list
    
    def traverse(self):
        tempNode=self.head
        if(tempNode is None):
            print("no link list found")
            return
        while(tempNode is not None):
            print(tempNode.get_data(),end="\t")
            tempNode=tempNode.get_next()
        print()    

    # method to search a given value in the list
    def search(self, value):
        tempNode=self.head
        found=False
        while(tempNode is not None):
            if(tempNode.get_data()==value):
                print("value found in list: ",value)
                found=True
                return
            else:
                tempNode=tempNode.get_next()
        else:
            print ("value not found in the list :",value)
            return

    #method to delete the nodes of linked list
    def delete(self,location):
        #when there is no linked list
        if(self.head is None):
            print("there is no liked list")
            return
        #when we want to delet the first node
        elif(location==0):
            self.head=self.head.get_next()
            self.nodeCount-=1
        #when we want to delete the last node
        elif(location==self.nodeCount):
            tempNode=self.head
            for i in range(0,self.nodeCount-2):
                tempNode=tempNode.get_next()
            tempNode.set_next(None)
            self.tail=tempNode
            self.nodeCount-=1
        #when we want to delete in between head and tail nodes
        else:
            tempNode=self.head
            for i in range(0,location-1):
                tempNode=tempNode.get_next()
            tempNode.set_next(tempNode.get_next().get_next())
            self.nodeCount-=1

    #method to delete entire linked list
    def deleteList(self):
        self.head=None
        self.tail=None





    






        



