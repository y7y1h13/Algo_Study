class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class MGR:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head.data == '':
            self.head = Node(data)
            self.tail = self.head

        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
            node.next.prev = node
            self.tail = node.next

    def search_to_head(self, data):
        node = self.head
        while node:
            if node.data == data:
                return True
            else:
                node = node.next
        return False

    def search_to_tail(self, data):
        node = self.tail
        while node:
            if node.data == data:
                return True
            else:
                node = node.prev
        return False

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    tmp = node.next
                    node.next = node.next.next
                    node.next.prev = node
                    del tmp
                else:
                    node = node.next


a = MGR(0)
for i in range(1, 10):
    a.insert(i)
print(a.search_to_head(1))
print(a.search_to_tail(10))
a.delete(3)
a.desc()
