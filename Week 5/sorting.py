#Tye Hickman
# Week 5
# Sorting and Searching questions

# consider these lists of integers:
# theList = [1,2,3,4,5,6,7,8,9,10]
theList = [10,4,9,8,7,5,6,3,2,1]

def bubbleSort(arr):
    numberOfExchanges = 0
    print("\nBubble Sort")
    print("\nStarting with this list: " + str(arr))
    # As larger numbers 'bubble up' we decrease the length of our array,
    # Using negative indexing the iteration narrows our list down to what 
    # has not been sorted.
    for passes in range(len(arr)-1,0,-1):
        for i in range(passes):
            # if our element is greater than the element in the next index,
            # we move it along or 'up' the list.
            if arr[i]>arr[i+1]:
                # temporarily hold the element to make the exchange
                # temp = arr[i]
                # # assign the element at next index to our current index
                # arr[i] = arr[i+1]
                # # assign the next index to our larger current index element
                # arr[i+1] = temp

                # Thank Crom for python's multi assignments...
                arr[i],arr[i+1] = arr[i+1],arr[i]
                #for fun, let's see what our list looks like after each exchange,
                print("Pass no. " + str(passes) + " - Exchange " + str(i+1) + ": " + str(arr))
                numberOfExchanges = numberOfExchanges + 1
    #Also for fun, let's see how many exchanges were made in total to sort the list:
    print("Total Exchanges: " + str(numberOfExchanges))
    

def selectionSort(arr):
    numberOfExchanges = 0
    print("\nSelection Sort")
    print("\nStarting with this list: " + str(arr))
    # as with bubble, we traverse our list in reverse so as the list size decreases,
    # we know our largest values are in the correct place
    for passes in range(len(arr)-1,0,-1):
        #Selection works by identifying the largest elements position 
        #then making an exchange
        indexOfLargest = 0
        for i in range(1,passes+1):
            #if our element at i is larger than the element at the largest
            #index we exchange them
            if arr[i]>arr[indexOfLargest]:
                indexOfLargest = i
            
        #use double assignment to make the actual exchange of elements
        arr[passes],arr[indexOfLargest] = arr[indexOfLargest],arr[passes]
        print("Pass no. " + str(passes) + " - Exchange " + str(i) + ": " + str(arr))
        numberOfExchanges = numberOfExchanges + 1

    #Again, let's show how many exchanges were made in total
    print("Total Exchanges: " + str(numberOfExchanges))

def insertionSort(arr):
    numberOfExchanges = 0
    print("\nInsertion Sort")
    print("\nStarting with this list: " + str(arr))
    # to begin assume the first item is our 'sorted' sublist
    for i in range(1,len(arr)):
        # for each element after our starting position, we 
        # advance through the list and do our comparison against the
        # expanding sublist
        currentVal = arr[i]
        pos = i
        # Here is where our comparison happens
        #if our current value is greater than the previous position, 
        # we know it needs to move to the left in the list so we decrement
        # position and compare again.
        while pos > 0 and arr[pos-1]>currentVal:
            arr[pos] = arr[pos-1]
            pos = pos-1
        # once we reach a value in the sublist that is less than our 
        # current value, we insert our current value
        arr[pos]=currentVal
        print("Pass no. " + str(i) + " - Exchange " + str(i) + ": " + str(arr))
        numberOfExchanges = numberOfExchanges + 1

    print("Total Exchanges: " + str(numberOfExchanges))


#Driver code:
def main():
    theFunction = input("\nWhich sort function? (B)ubble, (S)election, (I)nsertion ").lower()
    while theFunction not in ['b','s','i']:
        theFunction = input("\nWhich sort function? (B)ubble, (S)election, (I)nsertion ").lower()
    if theFunction == 'b':
        bubbleSort(theList)
    elif theFunction == 's':
        selectionSort(theList)
    else:
        insertionSort(theList)




main()