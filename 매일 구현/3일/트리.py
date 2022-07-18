class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class MGR:
    def __init__(self, data):
        self.head = data

    def insert(self, data):
        self.node = self.head
        while self.node:
            if data < self.node.data:
                if self.node.left is None:
                    self.node.left = Node(data)
                    break
                else:
                    self.node = self.node.left
            else:
                if self.node.right is None:
                    self.node.right = Node(data)
                    break
                else:
                    self.node = self.node.right

    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                return True
            elif data < node.data:
                node = node.left
            else:
                node = node.right
        return False

    def delete(self, data):
        self.node = self.head
        self.node_parent = self.head
        flag = False
        while self.node:
            if self.node.data == data:
                flag = True
                break

            elif data < self.node.data:
                self.node_parent = self.node
                self.node = self.node.left

            else:
                self.node_parent = self.node
                self.node = self.node.right

        if not flag:
            return False

        if self.node.left is None and self.node.right is None:
            if self.node_parent.data > self.node.data:
                self.node_parent.left = None
            else:
                self.node_parent.right = None
            del self.node

        elif self.node.left is None and self.node.right is not None:
            if self.node_parent.data > self.node.data:
                self.node_parent.left = self.node.right
            else:
                self.node_parent.right = self.node.right

        elif self.node.left is not None and self.node.right is None:
            if self.node_parent.data > self.node.data:
                self.node_parent.left = self.node.left
            else:
                self.node_parent.right = self.node.left

        else:
            self.min_node = self.node
            self.min_node_parent = self.node
            while self.min_node.left:
                self.min_node_parent = self.min_node
                self.min_node = self.min_node.left

            if self.min_node.right is not None:
                self.min_node_parent.left = self.min_node.right
                del self.min_node.right
                if self.min_node.data < self.node_parent.data:
                    self.node_parent.left = self.min_node
                else:
                    self.node_parent.right = self.min_node
                self.min_node.right = self.node.right
                self.min_node.left = self.node.left

            else:
                if self.min_node.data < self.node_parent.data:
                    self.node_parent.left = self.min_node
                else:
                    self.node_parent.right = self.min_node
                self.min_node.left = self.node.left
                self.min_node.right = self.node.right
            del self.min_node_parent.left
        return True

import random

# 0 - 999 중, 100개의 숫자
bst_nums = set()
while len(bst_nums) != 100:
    bst_nums.add(random.randint(0, 999))

# 선택된 100개의 숫자를 이진 탐색 트리에 입력
head = Node(500)
binary_tree = MGR(head)
for num in bst_nums:
    binary_tree.insert(num)

# 100개 검색
for num in bst_nums:
    if not binary_tree.search(num):
        print('search failer')

# 10개 삭제
delete_nums = set()
bst_nums = list(bst_nums)
while len(delete_nums) != 10:
    delete_nums.add(bst_nums[random.randint(0, 99)])

# 10개 삭제 확인
for del_num in delete_nums:
    if not binary_tree.delete(del_num):
        print('delete falied', del_num)
