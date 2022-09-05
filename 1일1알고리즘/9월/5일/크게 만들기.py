N, K = map(int, input().split())
n = K
a = list(map(int, input()))
stack = list()
for i in a:
    while stack and stack[-1] < i and n > 0:
        stack.pop()
        n -= 1
    stack.append(i)
print(*stack[:N-K], sep='')