import numpy as np 
import copy

Data = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]


def merge(left: list, right: list):
    left = left if left else []
    right = right if right else []

    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) > 0:
        for n in left:
            result.append(n)
    if len(right) > 0:
        for n in right:
            result.append(n)
    return result


def adjustHeap(data, idx):
    maxIndex = idx
    if 2*idx < len(data) and data[maxIndex] < data[2*idx]:
        maxIndex = 2*idx
    if 2*idx+1 < len(data) and data[maxIndex] < data[2*idx+1]:
        maxIndex = 2*idx + 1
    if maxIndex != idx:
        data[maxIndex], data[idx] = data[idx], data[maxIndex]
        adjustHeap(data, maxIndex)

def buildHeap(data: list):
    data = [0] + data
    idx = len(data) // 2
    while idx > 0:
        adjustHeap(data, idx)
        idx -= 1
    return data

class Sort:
    def __init__(self, data=None):
        self.data = data if data else Data
        self.size = len(self.data)

        self.bubble()
        self.select()
        self.insert()
        self.shell()
        self.merge()
        self.quick()
        self.heap()
        self.count()
        self.bucket()
        self.radix()

    def bubble(self, data=None):
        # T-avg: O(n^2), T-best: O(n), T-bad: O(n^2)
        # space: O(1)
        # In-place, Stable
        data = data if data else copy.deepcopy(self.data)

        for i in range(self.size - 1):     # 只需要 size - 1 次即可，最后一次只有一个元素来进行比较，用不着
            for j in range(self.size - i - 1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]

        print(f'bubble sort: {data}')
        return data

    def select(self, data=None):
        # T-avg: O(n^2), T-best: O(n^2), T-bad: O(n^2)
        # space: O(1)
        # In-place, Unstable
        data = data if data else copy.deepcopy(self.data)

        for i in range(self.size - 1):
            minIndex = i
            for j in range(i+1, self.size):
                if data[minIndex] > data[j]:
                    minIndex = j
            data[i], data[minIndex] = data[minIndex], data[i]
        
        print(f'select sort: {data}')
        return data

    def insert(self, data=None):
        # T-avg: O(n^2), T-best: O(n), T-bad: O(n^2)
        # space: O(1)
        # In-place, Stable
        data = data if data else copy.deepcopy(self.data)

        for i in range(1, self.size):
            for j in range(i, 0, -1):
                if data[j] < data[j-1]:
                    data[j], data[j-1] = data[j-1], data[j]

        print(f'insert sort: {data}')
        return data

    def shell(self, data=None):
        # T-avg: O(nlogn), T-best: O(n(logn)^2), T-bad: O(n(logn)^2)
        # space: O(1)
        # In-place, Unstable
        data = data if data else copy.deepcopy(self.data)

        gap = len(data) // 2
        while gap > 0:
            for i in range(gap, len(data)):
                for j in range(i, 0, -gap):
                    if j-gap >= 0 and data[j] < data[j-gap]:
                        data[j], data[j-gap] = data[j-gap], data[j]
            gap //= 2

        print(f'shell sort : {data}')
        return data
        
    def _merge(self, data=None):
        if data is None or len(data) == 0:
            return []
        if len(data) == 1:
            return data

        result = []
        mid = len(data) // 2
        left = self._merge(data[:mid])
        right = self._merge(data[mid:])
        res = merge(left, right)
        result.extend(res)
        return result
    
    def merge(self, data=None):
        # T-avg: O(nlogn), T-best: O(nlogn), T-bad: O(nlogn)
        # space: O(n)
        # Out-place, Stable
        # data = data if data else copy.deepcopy(self.data)
        data = data if data else copy.deepcopy(self.data)
        result = self._merge(data)
        print(f'merge sort : {result}')
        return result

    def _quick(self, data):
        if data is None or len(data) == 0:
            return []
        if len(data) == 1:
            return data
            
        result = []
        p = 0  # pivot
        i, j = 1, len(data) - 1
        while i < j:
            while i < j and data[i] <= data[p]:
                i += 1
            while i < j and data[j] >= data[p]:
                j -= 1
            if i < j:
                data[i], data[j] = data[j], data[i]
                i += 1
                j -= 1
        while i < len(data) and data[i] <= data[p]:
            i += 1
        data[p], data[i-1] = data[i-1], data[p]
        result.extend(self._quick(data[:i]))
        result.extend(self._quick(data[i:]))

        return result
        
    def quick(self, data=None):
        data = data if data else copy.deepcopy(self.data)

        result = self._quick(data)

        print(f'quick sort : {result}')
        return result
        
    def heap(self, data=None):
        data = data if data else copy.deepcopy(self.data)
        data = buildHeap(data)

        result = []
        while len(data) > 1:
            data[1], data[-1] = data[-1], data[1]
            result.insert(0, data.pop(-1))
            adjustHeap(data, 1)

        print(f'heap sort  : {result}')
        return result
        
    def count(self, data=None):
        data = data if data else copy.deepcopy(self.data)

        max_ = max(data)
        min_ = min(data)
        bias = -min_
        
        side = [0] * (max_ - min_ + 1)
        for n in data:
            side[n + bias] += 1

        index, i = 0, 0
        while index < len(data):
            if side[i] != 0:
                data[index] = i - bias
                side[i] -= 1
                index += 1
            else:
                i += 1

        print(f'count sort : {data}')
        return data
        
    def _bucket(self, data, bucketSize=10):
        if data is None or len(data) == 0:
            return []
        if len(data) == 1:
            return data

        Max, Min = max(data), min(data)
        bucketNum = (Max - Min) // bucketSize + 1
        bucketArr = [[] for _ in range(bucketNum)]
        for n in data:
            index = (n - Min) // bucketSize 
            bucketArr[index].append(n)

        result = []
        for tmp in bucketArr:
            if bucketNum == 1:
                bucketSize -= 1
            temp = self._bucket(tmp, bucketSize)
            result.extend(temp)

        return result

    def bucket(self, data=None):
        data = data if data else copy.deepcopy(self.data)

        result = self._bucket(data)

        print(f'bucket sort: {result}')
        return result
        
    def radix(self, data=None):
        data = data if data else copy.deepcopy(self.data)

        Max = max(data)
        numDigit = len(str(Max))

        mod, div = 10, 1
        bucketList = [[] for _ in range(10)]

        for _ in range(numDigit):
            for n in data:
                index = n % mod // div
                bucketList[index].append(n)

            index = 0
            for k in range(len(bucketList)):
                for t in bucketList[k]:
                    data[index] = t
                    index += 1
                bucketList[k].clear()

            mod *= 10
            div *= 10

        print(f'radix sort : {data}')
        return data

if __name__ == '__main__':
    Sort()
