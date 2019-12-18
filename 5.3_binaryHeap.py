class BinHeap:
    def __init__(self):
        self.headList = [0]
        self.currentSize = 0

    def __str__(self):
        return 'len: ' + str(self.currentSize) + '\t' + str(self.headList[1:])

    def percUp(self, idx):
        while idx//2 > 0 and  self.headList[idx // 2] > self.headList[idx]:
            tmp = self.headList[idx // 2]
            self.headList[idx // 2] = self.headList[idx]
            self.headList[idx] = tmp
            idx = idx // 2

    def insert(self, t):
        self.headList.append(t)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percDown(self, idx):
        while 2*idx <= self.currentSize:
            minIndex = idx
            if self.headList[2*idx] < self.headList[minIndex]:
                minIndex = 2*idx
            if 2*idx+1 <= self.currentSize and self.headList[2*idx+1] < self.headList[minIndex]:
                minIndex = 2*idx + 1
            if minIndex != idx:
                self.headList[minIndex], self.headList[idx] = self.headList[idx], self.headList[minIndex]
                idx = minIndex
            else:
                break

    def delMin(self):
        mindata = self.headList[1]
        self.headList[1] = self.headList[-1]
        self.headList.pop()
        self.currentSize -= 1
        self.percDown(1)

        return mindata

    def buildHeap(self, alist):
        self.currentSize = len(alist)
        self.headList = [0] + alist[:]
        idx = self.currentSize // 2
        while (idx > 0):
            self.percDown(idx)
            idx -= 1

if __name__ == '__main__':
    binheap = BinHeap()
    binheap.buildHeap([9, 5, 6, 2, 31, 1, 8, 3, 23, 43, 21, 77])
    print(binheap)

    binheap.delMin()
    print(binheap)
