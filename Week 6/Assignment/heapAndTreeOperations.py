from binaryHeap import BinHeap
import random

print("""\nThe heap order property is as follows: In a heap, 
for every node x with parent p, 
the key in p is smaller than or equal to the key in x\n""")

# Generate a random list of numbers.
myList = []
for i in range(0,10):
    n = random.randint(1,100)
    myList.append(n)

print("This is my list: " + str(myList))


# Make a heap and a tree
myHeap = BinHeap()


#insert the items in the list on the heap one at a time
for el in range(len(myList)):
    myHeap.insert(myList[el])
    print(myHeap.heaplist)

myHeap.printAsTreeIsh(myHeap.heaplist)



#using the same list as before, now with the buildHeap method:
myNewHeap = BinHeap()
myNewHeap.buildHeap(myList)

print("\nNew Heap from buildHeap:\n")
print(myNewHeap.heaplist)
myNewHeap.printAsTreeIsh(myNewHeap.heaplist)
