#Tye Hickman
#Week 3
#Recursion: Minimum and Maximum values of a sequence

def findMinMax( aList, i=0, mini= float('inf'), maxi= float('-inf')):
    e=aList[i]
    #element less than minimum
    if e < mini: mini = e
    #element more than maximum
    if e > maxi: maxi = e
    #base case
    if i == len(aList)-1:
        return (mini, maxi)
    else:
        return findMinMax(aList,i+1,mini,maxi)


def main():
    # elements = int(input("How many items? "))
    # theList =[]

    # for i in range(elements):
    #     ele = int(input("Enter a number: "))
    #     theList.append(ele)
    
    theList = [0,5,6,9,23,13,-6,-55]

    print(theList)

    print(findMinMax(theList))

main()
