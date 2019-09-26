from linkedlist import linklist 
link1=linklist()
# to create a linked list
link1.createList(4,0)
link1.createList(8,1)
link1.createList(12,2)
link1.createList(16,3)
link1.createList(20,4)
link1.createList(24,5)
link1.createList(28,6)
link1.createList(32,7)
link1.createList(36,8)
link1.createList(40,9)

# to traverse a linked list
link1.traverse()

# to search in liked list
link1.search(32)
link1.search(33)
link1.search(36)
print("node count is",link1.nodeCount)
# to create nodes at boundry point in linked list
link1.createList(2,0)
print(link1.nodeCount)
link1.traverse()

temp=link1.nodeCount
link1.createList(400,temp)
print(link1.nodeCount)
link1.traverse()
# to traverse the link list
 
print("deleting nodes:")
#to delete nodes
link1.delete(1)
link1.traverse()
print(link1.nodeCount)
link1.delete(8)
link1.traverse()
print(link1.nodeCount)


#to delete at boundry points in linked list
print("deleting at boundry points:")
link1.delete(link1.nodeCount)
link1.traverse()
print(link1.nodeCount)
link1.delete(0)
link1.traverse()
print(link1.nodeCount)

# to delete the entire list
link1.deleteList()
link1.traverse()




