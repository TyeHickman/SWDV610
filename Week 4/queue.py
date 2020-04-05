#Tye Hickman
# Week 4
# Queue

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    
    # Queues are First in First out so we can add to them just like a stack (enqueue)
    # But need to ensure that dequeue is only removing from the "rear" of the queue

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            self.items.pop()
            # pop() takes an option position parameter. If left blank, it defaults to -1
            # whish is the last item in a list, which is the FIRST IN for the queue

    def size(self):
        return len(self.items)

    def printQueue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            for item in self.items:
                print(str(self.items.index(item)) + " " +str(item))
                # print(item)

def main():
    myQueue = Queue()
    myQueue.printQueue()
    print(myQueue.isEmpty())
    print("--------------")
    myQueue.enqueue(1)
    myQueue.printQueue()
    print("--------------")
    myQueue.enqueue("Two")
    myQueue.printQueue()
    print(myQueue.size())
    print("--------------")
    myQueue.dequeue()
    myQueue.printQueue()






main()