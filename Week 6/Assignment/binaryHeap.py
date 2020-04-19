class BinHeap:
    def __init__(self):
        self.heaplist = [0]
        self.currentSize = 0

    def percUp(self,i):
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i//2]:
                # tmp = self.heaplist[i//2]
                # self.heaplist[i//2] = self.heaplist[i]
                # self.heaplist[i] = tmp
                self.heaplist[i//2],self.heaplist[i] = self.heaplist[i],self.heaplist[i//2]
            i = i//2

    def insert(self,k):
        self.heaplist.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heaplist[i] > self.heaplist[mc]:
                self.heaplist[i],self.heaplist[mc] = self.heaplist[mc],self.heaplist[i]
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heaplist[i*2] < self.heaplist[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heaplist.pop()
        self.percDown(1)
        return retval

    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heaplist = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

    # CAUTION: FOR DEMO PURPOSES ONLY
    def printAsTreeIsh(self,heapL):
        print("""
                 ___{}___
                /        \ 
              _{}_       _{}_
             /    \     /    \ 
            {}     {}  {}    {}
           /  \   / 
          {}  {} {}
        """.format(heapL[1],heapL[2],heapL[3],heapL[4],heapL[5],
        heapL[6],heapL[7],heapL[8],heapL[9],heapL[10]))