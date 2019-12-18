class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class biList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        # tmp = Node(data)
        # tmp.next = self.head
        # self.head = tmp
        self.insert_head(data)

    def insert(self, data):
        self.insert_head(data)
    
    def insert_head(self, data):
        tmp = Node(data)
        if self.head is None:
            self.head = tmp
            self.tail = tmp
        else:
            tmp.next = self.head
            self.head.previous = tmp
            self.head = tmp

    def insert_tail(self, data):
        tmp = Node(data)
        if self.tail is None:
            self.head = tmp
            self.tail = tmp
        else:
            tmp.previous = self.tail
            self.tail.next = tmp
            self.tail = tmp

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next

        return count

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            else:
                current = current.next
        
        return False

    def remove(self, data):
        current = self.head
        found = False
        while not found and current:
            if current.data == data:
                found = True
            else:
                current = current.next
        if not found:
            return False, f'not found {data}'

        if current.previous == None:
            self.head = current.next
            self.head.previous = None
        else:
            current.previous.next = current.next
            current.next.previous = current.previous

        return True

    def __str__(self):
        datalist = []
        current = self.head
        while current != None:
            tmp = [None, current.data, None]
            if current.previous:
                tmp[0] = current.previous.data
            if current.next:
                tmp[2] = current.next.data
            datalist.append(tmp)
            current = current.next
        
        return str(datalist)
        

if __name__ == '__main__':
    temp = Node(93)
    print(temp.data)

    mylist = biList()
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
    