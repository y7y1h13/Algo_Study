# 1. 링크드 리스트(추가, 삽입, 삭제, 출력) 구현
class LinkNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkMgr:
    def __init__(self, data):
        self.head = LinkNode(data)

    def insert(self, data):
        if self.head == '':
            self.head = LinkNode(data)
            return
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = LinkNode(data)
            return

    def insert1(self):
        node3 = LinkNode(2.5)
        node = self.head
        search = True
        while search:
            if node.data == 2:
                search = False
            else:
                node = node.next
        node_next = node.next
        node.next = node3
        node.next = node_next

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if self.head.data == '':
            print('x')
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