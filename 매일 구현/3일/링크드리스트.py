class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class MGR:
    def __init__(self, data):
        self.head = Node(data)

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def insert1(self):
        node1 = Node(1.5)
        node = self.head
        while node:
            if node.next.data == 1:
                tmp = node.next
                node.next = node1
                node1.next = tmp
                return True
            else:
                node = node.next

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if self.head.data == data:
            tmp = self.head
            self.head = self.head.next
            del tmp
            return True
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    tmp = node.next
                    node.next = node.next.next
                    del tmp
                else:
                    node = node.next


a = MGR(0)
for i in range(1, 10):
    a.insert(i)
a.insert1()
a.delete(3)
a.desc()
