class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class MGR:
    def __init__(self, head):
        self.current_node = None
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while self.current_node:
            if value < self.current_node.value:
                if self.current_node.left is None:
                    self.current_node.left = Node(value)
                    break
                else:
                    self.current_node = self.current_node.left
            else:
                if self.current_node.right is None:
                    self.current_node.right = Node(value)
                    break
                else:
                    self.current_node = self.current_node.right

    def search(self, value):
        self.current_node = self.head
        if self.current_node == '':
            return False
        while self.current_node:
            if self.current_node.value == value:
                return True

            elif value < self.current_node.value:
                self.current_node = self.current_node.left

            else:
                self.current_node = self.current_node.right
        return False


head = Node(1)
bst = MGR(head)
bst.insert(3)
bst.insert(5)
print(bst.search(3))
print(bst.search(4))