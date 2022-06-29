class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class MGR:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def delete(self, data):
        if self.head.data == '':
            print('데이터가 없습니다.')
            return

        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
            return

        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


link = MGR(0)
# link.delete(0)
# link.head
for i in range(1, 10):
    link.add(i)
link.delete(4)
link.delete(9)
link.desc()