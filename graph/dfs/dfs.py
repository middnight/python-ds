from nodes import node
from nodes import stack

class graph(object):
    def __init__(self,nodes=0):
        self.vertexList=[None for i in range(nodes)]  
        self.s1=stack() 
        self.list2=[0 for i in range(len(self.vertexList))] 
    
    def addEdge(self,fromNode,toNode):
        node1=node(toNode)
        if(self.vertexList[fromNode]==None):
            self.vertexList[fromNode]=node1
        else:
            tempNode=self.vertexList[fromNode]
            while(tempNode.get_next() is not None):
                tempNode=tempNode.get_next()
            tempNode.set_next(node1)
    
    def returnFirstUnVisitedNode(self,list1):
        for i in list1:
            if i==0:
                return i

    
    def dfs(self,startVertex):
        
        
        while(0 in self.list2):
            
            if(self.list2[startVertex]==0):
                self.s1.push(startVertex)
            else:
                return
            while(not self.s1.isEmpty()):
                tempVertex=self.s1.pop()
                if(self.list2[tempVertex]==0):
                    self.list2[tempVertex]=1
                    print(tempVertex,end="\t")
                tempNode=self.vertexList[tempVertex]
                while(tempNode is not None):
                    neighbour=tempNode.get_data()
                    self.dfs(neighbour)
                    if(self.list2[neighbour]==0):
                        self.s1.push(neighbour)
                    tempNode=tempNode.get_next()
