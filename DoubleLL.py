class DllNode:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None


class DoubleLL:
    def __init__(self):
        self.head = self.tail = None
        # tail - 0 элемент
        # head - последний
        self.len = 0

    def first_push(self, node):
        self.head = self.tail = node

    def push_to_start(self, node):
        if not self.head and not self.tail:
            self.first_push(node)
        else:
            self.tail.prev = node
            node.next = self.tail
            self.tail = node

    def push_to_end(self, node):
        if not self.head and not self.tail:
            self.first_push(node)
        else:
            self.head.next = node
            node.prev = self.head
            self.head = node

    def pop_from_start(self):
        if self.head and self.tail:
            self.tail = self.tail.next
            self.tail.prev = None
        else:
            raise Exception("Can't pop from empty DLL")

    def pop_from_end(self):
        if self.head and self.tail:
            self.head = self.head.prev
            self.head.next = None
        else:
            raise Exception("Can't pop from empty DLL")

    def get(self, index):
        if index > self.len - 1:
            raise Exception("Index out of range")
        else:
            i = 0
            tmp = self.tail
            while i < index:
                tmp = tmp.next
                i += 1
        return tmp.data

    def insert(self, index, node):
        if index > self.len and index != 0:
            raise Exception("Index out of range")
        else:
            if index == 0:
                self.push_to_start(node)
            elif index == self.len:
                self.push_to_end(node)
            else:
                    i = 0
                    tmp = self.tail
                    while i < index - 2:
                        tmp = tmp.next
                        i += 1
                    node.prev = tmp
                    node.next = tmp.next
                    tmp.next = node
            self.len += 1

    def delete(self, index):
        if index > self.len - 1 and index != 0:
            raise Exception("Index out of range")
        else:
            if index == 0:
                self.pop_from_start()
            elif index == self.len - 1:
                self.pop_from_end()
            else:
                i = 0
                tmp = self.tail
                while i < index - 1:
                    tmp = tmp.next
                    i += 1
                tmp.next = tmp.next.next
                tmp.next.prev = tmp

    def print_list(self):
        tmp = self.tail
        print('-----Data Start-----')
        while tmp is not None:
            print(tmp.data)
            tmp = tmp.next
            """if elem.prev:
                print('-----Previous data-----')
                print(elem.prev.data)
            if elem.next:
                print('-----Next Data-----')
                print(elem.next.data)"""
        print('-----Data End-----')
