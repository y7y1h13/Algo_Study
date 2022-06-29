# 2. 더블 링크드 리스트 구현

class DoubleNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoubleMgr:
    def __init__(self, data):
        self.head = DoubleNode(data)
        self.tail = self.head

    def insert(self, data):
        node = self.head
        while node.next:
            node = node.next
        node.next = DoubleNode(data)
        node.next.prev = node
        self.tail = node.next

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
        if self.tail is None:
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
        while node.next:
            print(node.data)
            node = node.next

    def insert_before(self, data, before_data):
        if self.head is None:
            self.head = DoubleNode(data)
            return True
        else:
            node = self.head
            while node:
                if node.data == before_data:
                    temp = node.next
                    new = DoubleNode(data)
                    node.next = new
                    new.prev = node
                    new.next = temp
                    temp.prev = new
                    return True
                else:
                    node = node.next


d = DoubleMgr(0)
for i in range(1, 10):
    d.insert(i)
# d.desc()
d.insert_before(2.5, 2)
# print(d.search_from_tail(2.5).data)
d.desc()