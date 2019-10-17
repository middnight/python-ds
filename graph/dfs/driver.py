from dfs import graph
from nodes import stack
g1=graph(4)
g1.addEdge(0,1)
g1.addEdge(0,2)
g1.addEdge(1,2)
g1.addEdge(2,0)
g1.addEdge(2,3)
g1.addEdge(3,3)

#g1.dfs(2)
print()
g1.dfs1(2)
print()



g2=graph(6)
g2.addEdge(0,1)
g2.addEdge(0,2)
g2.addEdge(1,0)
g2.addEdge(1,3)
g2.addEdge(1,4)
g2.addEdge(2,0)
g2.addEdge(2,4)
g2.addEdge(3,1)
g2.addEdge(3,4)
g2.addEdge(3,5)
g2.addEdge(4,3)
g2.addEdge(4,2)
g2.addEdge(4,1)
g2.addEdge(4,5)
g2.addEdge(5,3)
g2.addEdge(5,4)

#g2.dfs(2)
print()
g2.dfs1(2)
print()

