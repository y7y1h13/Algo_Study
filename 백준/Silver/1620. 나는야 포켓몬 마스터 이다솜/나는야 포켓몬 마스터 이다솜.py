import sys


input = sys.stdin.readline

N, M = map(int, input().split())
name = {}
num = []
for i in range(N):
    k = input().rstrip()
    name[k] = i + 1
    num.append(k)

for _ in range(M):
    t = input().rstrip()
    if t.isalpha():
        print(name[t])
    else:
        print(num[int(t) - 1])