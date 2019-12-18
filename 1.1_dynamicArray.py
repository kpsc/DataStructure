class DynamicArray:
    def __init__(self, capacity):
        self.data = []
        self.size = 0              # 当前数组长度
        self.capacity = capacity   # 数组最大容量

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
        return f'capacity: {self.capacity}\tsize: {self.size}\t{str(self.data)}'

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
        if self.size == self.capacity:
            self.capacity *= 2
        self.data.append(d)
        self.size += 1
        return True

    def delete(self, value):
        try:
            self.data.remove(value)
            self.size -= 1
            if self.size <= self.capacity // 2:
                self.capacity = self.capacity // 2
            return True
        except ValueError:
            return False
    

if __name__ == '__main__':
    arr = DynamicArray(5)

    for d in [3, 4, 5, 9, 10]:
        arr.add(d)
    print(arr)
    
    print(f'find 9 in array: {arr.find(9)}')
    print(f'find 123 in array: {arr.find(123)}')
    print('add 7: ', arr.add(7), '\t ', arr)
    print('delete 4: ', arr.delete(4), '\t', arr)
    print('delete 11:', arr.delete(11), '\t',  arr)
