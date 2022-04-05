from collections import Counter
N = int(input())
a = list(map(int, input().split()))
ans = [-1] * N
counter = Counter(a)
stack = [0]
for i in range(N):
    while stack and counter[a[stack[-1]]] < counter[a[i]]:
        ans[stack.pop()] = a[i]
    stack.append(i)
print(*ans)