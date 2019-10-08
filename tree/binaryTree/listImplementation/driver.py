from tree import binaryTree

tree1=binaryTree()

print("inserting nodes in binary tree")
tree1.insertNode(10)
tree1.insertNode(20)
tree1.insertNode(30)
tree1.insertNode(40)
tree1.insertNode(50)
tree1.insertNode(60)
tree1.insertNode(70)
tree1.insertNode(80)
tree1.insertNode(90)
tree1.insertNode(100)

print("traversing the nodes")

tree1.traversal()
print("the tree is empty :",tree1.isEmpty())
print("performing serach in tree")
tree1.search(10)
tree1.search(50)
tree1.search(200)
print("deleteing elements from the tree")

tree1.traversal()
tree1.deleteNode(20)
tree1.traversal()
tree1.deleteNode(40)
tree1.traversal()
tree1.deleteNode(70)
tree1.traversal()
tree1.deleteNode(60)
tree1.traversal()
#tree1.deleteNode(10)
#tree1.traversal()
tree1.deleteNode(50)
#tree1.deleteNode()
#tree1.deleteNode()


tree1.traversal()

