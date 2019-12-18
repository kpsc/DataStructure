class DynamicArray:
    def __init__(self, size):
        self.data = [None] * size
        self.size = size    # 数组长度

    def __getitem__(self, index):
        try:
            assert (index < self.size), 'index out of range'
            return self.data[index]
        except IndexError:
            print('error: index out of range')
            return None

    def __setitem__(self, index, value):
        try:
            assert (index < self.size), 'index out of range'
            self.data[index] = value
        except IndexError:
            print('error: index out of range')

    def __str__(self):
        return f'size: {self.size}\t{str(self.data)}'

    def __len__(self):
        return self.size

    def __iter__(self):
        for item in self.data:
            yield item

    def find(self, value):
        try:
            for item in self.data:
                if item == value:
                    return True
            return False
        except:
            return False

    def add(self, d):
        if self.data[0] is None:
            self.data[0] = d
            return True
        if self.data[-1] is not None:
            print('out of array size')
            return False
            
        tmp = self.size - 2
        while  tmp >= 0 and self.data[tmp] is None:
            tmp -= 1
            
        while  tmp >= 0 and d < self.data[tmp]:
            self.data[tmp+1] = self.data[tmp]
            tmp -= 1 
        self.data[tmp+1] = d
        return True

    def delete(self, value):
        flag = False
        for idx, item in enumerate(self.data):
            if item == value:
                self.data[idx] = None
                flag = True
                break
        for i in range(idx, self.size-1):
            self.data[i] = self.data[i+1]
            if self.data[i] is None:
                break
        self.data[-1] = None
        return flag
    

if __name__ == '__main__':
    arr = DynamicArray(5)

    for d in [7, 3, 4, 9, 2]:
        arr.add(d)
    print(arr)
    
    print(f'find 9 in array: {arr.find(9)}')
    print(f'find 123 in array: {arr.find(123)}')
    print('add 7: ', arr.add(7), '\t ', arr)
    print('delete 4: ', arr.delete(4), '\t', arr)
    print('delete 11:', arr.delete(11), '\t',  arr)

    print('add 1: ', arr.add(1), '\t ', arr)
