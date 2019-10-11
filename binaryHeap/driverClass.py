from binaryHeap import binaryHeap
print("creating a min binary heap")
tree1=binaryHeap()
tree1.insert(348)
tree1.insert(333)
tree1.insert(334)
tree1.insert(334)
tree1.insert(332)
tree1.insert(3425)
tree1.insert(336)
tree1.insert(3436)
tree1.insert(323)
tree1.insert(3647)
tree1.insert(375)
tree1.insert(329)
tree1.insert(331)

print("traversing the heap")
tree1.traverse()
print("top of heap is",tree1.peekOfHeap())
print("size of heap is", tree1.sizeOfHeap())

print("deleting the root from heap")
tree1.extract()
print("traversing the heap")
tree1.traverse()
print("top of heap is",tree1.peekOfHeap())
print("size of heap is", tree1.sizeOfHeap())

print("deleting the root from heap")
tree1.extract()
print("traversing the heap")
tree1.traverse()
print("top of heap is",tree1.peekOfHeap())
print("size of heap is", tree1.sizeOfHeap())





