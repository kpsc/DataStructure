class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class OrderedList:
    def __init__(self, order=True):
        self.head = None
        self.order = order

    def add(self, data):
        tmp = Node(data)
        current = self.head
        previous = None
        while current and current.data < data:
            previous = current
            current = current.next
        tmp.next = current
        if previous == None:
            self.head = tmp
        else:
            previous.next = tmp

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next

        return count

    def search(self, data):
        current = self.head
        found = False
        while current and not found:
            if current.data == data:
                return True
            else:
                current = current.next
        
        return False

    def remove(self, data):
        current = self.head
        previous = None
        found = False
        while not found and current:
            if current.data == data:
                found = True
            else:
                previous = current
                current = current.next
        if not found:
            return False, f'not found {data}'

        if previous == None:
            self.head = current.next
        else:
            previous.next = current.next

        return True

    def __str__(self):
        datalist = []
        current = self.head
        while current != None:
            datalist.append(current.data)
            current = current.next
        
        return str(datalist)
        

if __name__ == '__main__':
    temp = Node(93)
    print(temp.data)

    mylist = OrderedList()
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)

    print('unorderlist: ', mylist)
    print('isEmpty: ', mylist.isEmpty())
    print('size: ', mylist.size())
    print('search 26: ', mylist.search(26))
    print('search 18: ', mylist.search(18))

    print('remove 26: ', mylist.remove(26))
    print('search 26: ', mylist.search(26))
    print('unorderlist: ', mylist)
    print('remove 26: ', mylist.remove(26))
    