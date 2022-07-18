# class Node:
#     def __init__(self, d_l, d_r, left = None, right = None):
#         self.d_l = d_l
#         self.d_r = d_r
#         self.left = left
#         self. right = right
#
#
# class NodeMgr:
#     def __init__(self, data):
#         self.head = Node(data[0], data[1])
#         self.cnt = 0
#         self.node = self.head
#
#     def insert(self, data):
#         while self.node:
#             if self.node.d_r <= data[0]:
#                 self.node = self.node.right
#             else:
#                 self.node = self.node.left
#         if self.node.d_r <= data[0]:
#             self.node.right = Node(data[0], data[1])
#         else:
#             self.node.left = Node(data[0], data[1])
#
#     def ans(self, node):
#         if node.left:
#             self.cnt += 1
#             self.ans(node.left)
#         else:
#             self.ans(node.right)
#
#
# if __name__ == "__main__":
#     a = list()
#     N = int(input())
#     for i in range(N):
#         S = list(map(int, input().split()))
#         a.append(S)
#         if i == 0:
#             n = NodeMgr(S)
#         else:
#             NodeMgr.insert(S)
#         if i == N - 1:

import heapq
from sys import stdin

input = stdin.readline


def solution():
    a = sorted([list(map(int, input().split()))for _ in range(int(input()))])
    r = [-1]
    for s, e in a:
        if s < r[0]:
            heapq.heappush(r, e)
        else:
            heapq.heapreplace(r, e)
    return len(r)


if __name__ == "__main__":
    print(solution())
