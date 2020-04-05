#Tye Hickman
#Week 4 
#Implement a Stack

class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.items.insert(0,item)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.items.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "Nothing in Stack"
        else:
            return self.items[0]

    def size(self):
        return len(self.items)

    def printStack(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            for item in self.items:
                print(str(self.items.index(item)) + " " +item)
                # print(item)



def main():
    myStack = Stack()
    print(myStack.isEmpty())
    print(myStack.pop())
    print("--------------")
    myStack.push("Toilet Paper")
    print(myStack.peek())
    print(myStack.size())
    print("--------------")
    myStack.push("Hand Sanitizer")
    print(myStack.peek())
    print(myStack.size())
    myStack.printStack()
    print("--------------")
    myStack.pop()
    print(myStack.peek())
    print(myStack.size())
    print(myStack.isEmpty())

main()