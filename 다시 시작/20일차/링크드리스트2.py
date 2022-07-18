class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeMGR:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def insert(self):
        node3 = Node(1.5)
        node = self.head
        search = True
        while search:
            if node.data == 1:
                search = False
            else:
                node = node.next
        node_next = node.next
        node.next = node3
        node3.next = node_next


link = NodeMGR(0)
for i in range(1, 10):
    link.add(i)
link.insert()
link.desc()
