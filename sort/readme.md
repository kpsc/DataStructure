# SORT

<p align='center'>
    <img src='../images/sort.jpg' width=90%>
</p>



- ## Bubble Sort

  ```python
  # 比较相邻元素，若前面比后面大，则交换其位置，第一次后可找到最大值
  # 重复以上步骤，每次比较到 -i 个
  def bubble(self, data=None):
      # T-avg: O(n^2), T-best: O(n), T-bad: O(n^2)
      # space: O(1)
      # In-place, Stable
      data = data if data else copy.deepcopy(self.data)
      for i in range(self.size - 1): # 只需要 size - 1 次即可，最后一次只有一个元素来进行比较，用不着
          for j in range(self.size - i - 1):
              if data[j] > data[j+1]:
                  data[j], data[j+1] = data[j+1], data[j]
  
  	print(f'bubble sort: {data}')
      return data
  ```
  <p align='center'>
      <img src='../images/bubble.gif' width=100%>
  </p>



- ## Select Sort

  ```python
  # 每次选择最小的一个值，与第 i 个元素交换位置
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
  ```
  <p align='center'>
      <img src='../images/select.gif' width=100%>
  </p>



- ## Insert Sort

  ```python
  # 从第一个元素开始，默认有序
  # 取下一个元素，与已经排序的元素序列从后向前比较，若小于前面的元素，则交换位置
  # 递归将剩下的元素加入到前面有序序列中
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
  ```
  <p align='center'>
      <img src='../images/insert.gif' width=100%>
  </p>



- ## Shell Sort

  ```python
  # 插入排序的升级版
  # 设置一个增量序列 t1, t2, ti, tj, tk, ti > tj, tk=1
  # 按增量序列个数k， 对序列进行 k 趟排序
  # 间隔 ti 的序列进行插入排序
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
  ```
  <p align='center'>
      <img src='../images/shell.jpeg' width=100%>
  </p>



- ## Merge Sort

  ```python
  # 将长度为 n 的序列分割长度为 n/2 的两个子序列
  # 对这两个子序列分别进行归并排序
  # 合并有序序列
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
  ```
  <p align='center'>
      <img src='../images/merge.gif' width=100%>
  </p>



- ## Quick Sort

  ```python
  # 从序列中选择一个元素，作为基准(pivot)
  # 对序列重新排列，所有比基准小的元素放在基准前面，比基准大的放在基准后面，处理完后，基准处于中间位置
  # 以基准为分界点，递归对左边和右边子序列进行排序
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
  ```
  <p align='center'>
      <img src='../images/quick.gif' width=100%>
  </p>



- ## Heap Sort

  ```python
  # 将初始序列构造成大顶堆
  # 将堆顶元素与序列最后一个元素进行位置交换，重新调整堆(不包换最后一个位置)，重新形成大顶堆
  # 重复以上步骤，直到堆为空
  
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
  ```
  <p align='center'>
      <img src='../images/heap-1.gif' width=100%>
  </p>



- ## Count Sort

  ```python
    # 找出序列中的最大值和最小值
    # 统计序列中值为 i 的元素出现的次数，加入到辅助数组中
    # 反向填充
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
  ```
  <p align='center'>
      <img src='../images/count.gif' width=100%>
  </p>



- ## Bucket Sort

  ```python
    # 人为设置桶的大小，作为每个桶能放多少种不同的数值(容量不限)
    # 将序列中的数据放入到桶中
    # 对每个桶进行排序
    # 将不为空的桶的数据合并
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
  ```
  <p align='center'>
      <img src='../images/bucket.png' width=100%>
  </p>



- ## Radix Sort

  ```python
    # 取得序列中的最大值，得到位数，并设置大小为10的辅助序列
    # 从最低位开始，将原始序列按位的大小加入到辅助序列中
    # 对辅助序列中的数据利用计数排序的思路，恢复到原序列中
    # 递归上最高位重复步骤2-3
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
  ```
  <p align='center'>
      <img src='../images/radix.gif' width=100%>
  </p>
  
  