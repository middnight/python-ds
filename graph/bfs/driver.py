from bfs import graph

g1=graph(4)
g1.addEdge(0,1)
g1.addEdge(0,2)
g1.addEdge(1,2)
g1.addEdge(2,0)
g1.addEdge(2,3)
g1.addEdge(3,3)

list1=g1.bfs(2)

print("breadth first search oreder is:",list1)

print()
g1=graph(8)
g1.addEdge(0,1)
g1.addEdge(0,2)
g1.addEdge(0,3)
g1.addEdge(1,4)
g1.addEdge(2,5)
g1.addEdge(3,6)
g1.addEdge(4,7)
g1.addEdge(5,7)
g1.addEdge(6,7)
list1=g1.bfs(0)

print("breadth first search oreder is:",list1)
