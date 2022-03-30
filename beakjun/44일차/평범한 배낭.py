N, K = map(int, input().split())
a = [0] * (K+1)

for _ in range(N):
    w, v = map(int ,input().split())
    for j in range(K, w-1, -1):
        a[j] = max(a[j], a[j-w] + v)
print(a[-1])