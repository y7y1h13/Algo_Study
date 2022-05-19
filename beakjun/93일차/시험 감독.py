N = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
ans = 0
for i in a:
    k = i
    ans += 1
    k -= b
    if k <= 0:
        continue
    elif k % c == 0:
        ans += k // c
    else:
        ans += (k // c) + 1
print(ans)