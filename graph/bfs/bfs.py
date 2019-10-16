from linkList import node
from linkList import queue
class graph(object):
    def __init__(self,nodes=0):
        self.list1=[None for x in range(nodes)]
        self.vertexCount=nodes

    def addEdge(self,fromNode,toNode):
        if(self.list1[fromNode]==None):
            node1=node(toNode)
            self.list1[fromNode]=node1
        else:
            node1=node(toNode)
            tempNode=self.list1[fromNode]
            while(tempNode.get_next() is not None):
                tempNode=tempNode.get_next()
            tempNode.set_next(node1)
        
    def getNeighbours(self,ofNode):
        tempNode=self.list1[ofNode]
        vertexList=list()
        while(tempNode is not None):
            vertexList.append(tempNode.get_data())
            tempNode=tempNode.get_next()
        #print(vertexList)
        return vertexList

    def returnFirstUnvisitedNode(self,list1):
        for i in list1:
            if(i==0):
                return i
        

    def bfs(self,startVertex):
        list2=[0 for i in range(self.vertexCount)]
        bfsTraversal=list()
        q=queue()
        while(0 in list2):
            if(list2[startVertex]==0):
                q.enQueue(startVertex)
            else:
                q.enQueue(self.returnFirstUnvisitedNode(list2))
            while(not q.isEmpty()):
                vertex=q.deQueue()
                if(list2[vertex]==0):
                    list2[vertex]=1
                    bfsTraversal.append(vertex)
                neighbourNodes=self.getNeighbours(vertex)
                for i in neighbourNodes:
                    if(list2[i]==0):
                        q.enQueue(i)

        return bfsTraversal

