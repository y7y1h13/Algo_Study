# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left) + 1
        right = self.dfs(root.right) + 1

        return max(left, right)


root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
sol = Solution()
print("The max depth is:", sol.maxDepth(root))
