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

    def delete(self, value):
        searched = False
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif self.current_node.value > value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right

        if not searched:
            return False

        # self.current_node가 삭제할 Node, self.parent는 삭제할 Node의 Parent Node
        if self.current_node.left is None and self.current_node.right is None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.current_node

        # 자식을 하나 가지고 있을 때
        elif self.current_node.left is not None and self.current_node.right is None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left

        elif self.current_node.right is not None and self.current_node.left is None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

        # 자식이 두개
        # 1. 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 삭제할 Node의 Parent를 가리키도록 한다.
        elif self.current_node.left is not None and self.current_node.right is not None:
            while self.min_node.left:
                self.min_parent = self.min_node
                self.min_node = self.min_node.left
            if self.min_node.right is not None:
                self.min_parent.left = self.min_node.right
                del self.min_node.right
                if self.min_node.value < self.parent.value:
                    self.parent.left = self.min_node.value
                else:
                    self.parent.right = self.min_node.value
                self.min_node.left = self.current_node.left
                self.min_node.right = self.current_node.right
            # 최소값의 자식이 없음
            else:
                if self.min_node.value < self.parent.value:
                    self.parent.left = self.min_node.value
                else:
                    self.parent_right = self.min_node.value
                self.min_node.left = self.current_node.left
                self.min_node.right = self.current_node.right
            del self.min_parent.left
        return True

        # 2. 삭제할 Node의 왼쪽 자식 중, 가장 큰 값을 삭제한 Node의 Parent를 가리키도록 한다.


# head = Node(31)
# a = MGR(head)
# a.insert(15)
# a.insert(41)
# a.insert(13)
# a.insert(18)
# a.insert(11)
# a.insert(12)
# a.insert(16)
# a.insert(19)
# a.insert(17)
# a.insert(40)
# a.insert(51)
# a.delete(15)
# print(a.parent.left)
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