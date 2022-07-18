class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class MGR:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def search_from_head(self, data):
        if self.head is None:
            return False

        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False

    def search_from_tail(self, data):
        if self.head is None:
            return False

        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def insert_before(self, data, before_data):
        if self.head is None:
            self.head = Node(data)
            return True
        else:
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node is None:
                    return False
            new = Node(data)
            before_new = node.prev
            before_new.next = new
            new.next = node
            new.prev = before_new
            node.prev = new
            return True


double = MGR(0)
for i in range(1, 10):
    double.insert(i)
# double.desc()

data3 = double.search_from_tail(3)
# print(data3.data)

double.insert_before(1.5, 2)
# double.desc()

print(double.search_from_tail(1.5).data)