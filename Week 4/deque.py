# Tye Hickman
# Week 4
# Deque

class Deque:
    def __init__(self):
        self.items= []

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def addFront(self,item):
        self.items.append(item)
    
    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        if self.isEmpty():
            return "Deque is empty"
        else:
            self.items.pop()
    
    def removeRear(self):
        if self.isEmpty():
            return "Deque is empty"
        else:
            self.items.pop(0)

    def size(self):
        return len(self.items)
    
    def printDeque(self):
        if self.isEmpty():
            print("Deque is empty")
        else:
            for item in self.items:
                print(str(self.items.index(item)) + " " +item)
                # print(item)


def main():
    d = Deque()
    print(d.isEmpty())
    print(d.size())
    print("--------------")
    d.addFront("ONE")
    d.printDeque()
    d.addFront("TWO")
    d.printDeque()
    print("--------------")
    d.addRear("Cat")
    d.printDeque()
    print("--------------")
    d.removeFront()
    d.printDeque()
    print("--------------")
    d.removeRear()
    d.addRear("Dog")
    d.printDeque()
    print("--------------")
    



main()