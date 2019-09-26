from circularDoubleLL import circularDoubleLL

print("creating link list")
link1=circularDoubleLL()
link1.createList(3,0)
link1.createList(6,1)
link1.createList(9,2)
link1.createList(12,3)
link1.createList(15,4)
link1.createList(18,5)
link1.createList(21,6)
link1.createList(24,7)
link1.createList(27,8)
link1.createList(30,9)
#adding 2 at position 1
link1.createList(2,1)

print("traversing the link list")
link1.traverse()
print("no of nodes:",link1.nodeCount)
print("reverse traversing in link list")
link1.reverseTraverse()
print("no of nodes:",link1.nodeCount)

print("testing the circular feature of the list")
link1.test()
print("testing the reverse circular feature of the list")
link1.revTest()

print("searching some values in the linked list")
link1.search(4)
link1.search(8)
link1.search(12)
link1.search(16)

link1.traverse()
print("deleting the nodes")
link1.deleteNode(0)
link1.traverse()
print("no of nodes :",link1.nodeCount)

link1.deleteNode(4)
link1.traverse()
print("no of nodes :",link1.nodeCount)

link1.deleteNode(6)
link1.traverse()
print("no of nodes :",link1.nodeCount)

link1.deleteNode(link1.nodeCount)
link1.traverse()
print("no of nodes :",link1.nodeCount)

print("testing the circular feature of the list")
link1.test()
print("testing the reverse circular feature of the list")
link1.revTest()

print("deleting the entire list")
link1.deleteList()

print("testing the circular feature of the list")
link1.test()
print("testing the reverse circular feature of the list")
link1.revTest()


print("traversing the link list")
link1.traverse()
print("no of nodes:",link1.nodeCount)
print("reverse traversing in link list")
link1.reverseTraverse()
print("no of nodes:",link1.nodeCount)