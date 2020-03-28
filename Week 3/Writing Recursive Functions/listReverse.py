#Tye Hickman
#Week 3
#Recursion: Reverse a list recursively

def listReversal(aList, i=0):
    # can't a reverse a list of one
    if len(aList) == 1:
        return aList
    # base case = i = length of the list
    # which means we've gone through the entire list
    if len(aList) == i:
        return aList
    else:
        ele = aList.pop()
        aList.insert(i,ele)
        return listReversal(aList,i+1)



def main():
    theList = [1,2,3,4,5,6,7,8,9,10]
    # theList = ["one","two","three","four","five"]
    # theList = ['a','b','c','d','e']
    # theList = [1,'a',56.99,"Karma",-980,"Cat"]
    # theList = ["Charmander"]
    # theList = []

    print(listReversal(theList))


main()