from queue import queueList

print("creating the queue")
queue1=queueList()
queue1.enQueue(3)
queue1.enQueue(6)
queue1.enQueue(9)
queue1.enQueue(12)
queue1.enQueue(15)
queue1.enQueue(18)
queue1.enQueue(21)
queue1.enQueue(24)
queue1.enQueue(27)
queue1.enQueue(30)
print("printing the queue")
queue1.printQueue()

print("deQueuing the elements")
queue1.deQueue()
queue1.deQueue()
queue1.deQueue()
queue1.deQueue()

print("printing the queue")
queue1.printQueue()


print("deleting the queue")
queue1.deleteQueue()


print("checking if the queue is empty")
queue1.isEmpty()

print("printing the queue")
queue1.printQueue()
