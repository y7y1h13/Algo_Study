class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class MGR:
    def __init__(self, data):
        self.head = Node(data)

    # 추가
    def add(self, data):
        if self.head.data == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    # 출력
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    # 삽입
    def insert(self):
        node3 = Node(1.5)
        node = self.head
        while node:
            if node.data == 1:
                temp = node.next
                node.next = node3
                node3.next = temp
                return
            else:
                node = node.next

    # 삭제
    def delete(self, data):
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
            return

        else:
            node = self.head
            while node:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next


a = MGR(0)
for i in range(1, 10):
    a.add(i)
a.delete(9)
a.insert()
a.desc()