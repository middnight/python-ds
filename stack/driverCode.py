# this is the driver code for stack
from stack import stack

print("creating stack")
stack1=stack()
stack1.push(5)
stack1.push(10)
stack1.push(15)
stack1.push(20)
stack1.push(25)
stack1.push(30)
stack1.push(35)
stack1.push(40)
stack1.push(45)
stack1.push(50)

print("travesing the stack")
stack1.traverseStack()

print("popping-up the elements from stack ")
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()

print("travesing the stack")
stack1.traverseStack()
print("checking if the stack is empty")
stack1.isEmpty()

print("deleting the stack")
stack1.deleteStack()

print("travesing the stack")
stack1.traverseStack()

print("checking if the stack is empty")
stack1.isEmpty()
