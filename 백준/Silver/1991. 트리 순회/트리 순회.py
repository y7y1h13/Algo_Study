class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def pre(node):
    print(node.data, end='')
    if node.left != '.':
        pre(tree[node.left])
    if node.right != '.':
        pre(tree[node.right])


def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.data, end='')
    if node.right != '.':
        inorder(tree[node.right])


def post(node):
    if node.left != '.':
        post(tree[node.left])
    if node.right != '.':
        post(tree[node.right])
    print(node.data, end='')


N = int(input())
tree = {}
for _ in range(N):
    d, l, r = input().split()
    tree[d] = Node(d, l, r)

pre(tree['A'])
print()
inorder(tree['A'])
print()
post(tree['A'])