class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class MGR:
    def __init__(self, head):
        self.current_node = None
        self.head = head

    def insert(self, data):
        self.current_node = self.head
        while self.current_node:
            if data < self.current_node.data:
                if self.current_node.left is None:
                    self.current_node.left = Node(data)
                    break
                else:
                    self.current_node = self.current_node.left

            else:
                if self.current_node.right is None:
                    self.current_node.right = Node(data)
                    break
                else:
                    self.current_node = self.current_node.right

    def search(self, data):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.data == data:
                return True
            if data < self.current_node.data:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

    def delete(self, data):
        flag = False
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            if self.current_node.data == data:
                flag = True
                break
            elif data < self.current_node.data:
                self.current_node = self.current_node.left
                self.parent = self.current_node
            else:
                self.current_node = self.current_node.right
                self.parent = self.current_node

        if not flag:
            return False

        # 자식이 없음 경우
        if self.current_node.left is None and self.current_node.right is None:
            if data < self.parent.data:
                self.parent.data.left = None
            else:
                self.parent.data.right = None
            del self.current_node

        # 자식이 한명
        elif self.current_node.left is None and self.current_node.right is not None:
            if data < self.parent.data:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right
        elif self.current_node.left is not None and self.current_node.right is None:
            if data < self.parent.data:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.right
        
        # 자식이 두명
        elif self.current_node.left is not None and self.current_node.right is not None:
            
            # 가장 작은 자식이 자식을 가짐
            self.min_node = self.current_node.right.left
            self.min_node_parent = self.current_node.right
            while self.min_node.left:
                self.min_node_parent = self.min_node
                self.min_node = self.min_node.left
            if self.min_node.right is not None:
                self.min_node_parent.left = self.min_node.right
                if self.min_node.data < self.parent.data:
                    self.parent.left = self.min_node
                else:
                    self.parent.right = self.min_node
                self.min_node.left = self.current_node.left
                self.min_node.right = self.current_node.right
            else:
                if self.min_node.data < self.parent.data:
                    self.parent.left = self.min_node
                else:
                    self.parent.right = self.min_node
                self.min_node.left = self.current_node.left
                self.min_node.right = self.current_node.right
            del self.min_node_parent.left
            del self.current_node
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