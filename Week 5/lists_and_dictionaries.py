# Tye Hickman
# Week 5 
# Lists and dictionaries

# One of the main ways that a list differs from a dictionary is that
# Lists use indexes to navigate
favBooks = ["Lord of the Rings","Ender's Game","The Name of the Wind"]
print(favBooks[2])

# Dictionaries use key/value pairs to navigate
favoriteThings = {}
# Adding to a dictionary you specify the 'key' they would would like to use 
# To reference the value: myDictionary[key] = "value"
favoriteThings["Books"] = favBooks

def makeAList():
    listName = input("What is the list name? ")
    listLength = int(input("How many items in " + listName + "? "))
    theList = list()
    for i in range(listLength):
        item = input("List item: ")
        theList.append(item)
    return listName, theList


def main():
    #Let's add some lists to our dictionary
    numLists = int(input("How many lists to make? "))
    for i in range(numLists):
        print("\nList number " + str(i+1))
        theList = makeAList()
        print(theList)
        print(type(theList))
        favoriteThings[theList[0]] = theList[1]
    #Let's print our favorite things by list
    for key, value in favoriteThings.items():
        print(key, " : ", value)

main()