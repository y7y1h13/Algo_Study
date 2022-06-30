class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class MGR:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    # 추가
    def insert(self, data):
        if self.head.data == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
            node.next.prev = node
            self.tail = node.next

    # 출력
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    # 검색
    def search_to_head(self, data):
        node = self.head
        while node:
            if node.data == data:
                return True
            node = node.next
        return False

    def search_to_tail(self, data):
        node = self.tail
        while node:
            if node.data == data:
                return True
            node = node.prev
        return False

    # 삭제
    def delete(self, data):
        node = self.head
        while node:
            if node.next.data == data:
                temp = node.next
                node.next = node.next.next
                node.next.prev = node
                del temp
                return True
            else:
                node = node.next
        return False


a = MGR(0)
for i in range(1, 10):
    a.insert(i)
print(a.search_to_tail(3))
print(a.search_to_head(10))
a.delete(3)
a.desc()