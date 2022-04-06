a = list(input())
ans = [0] * 26

while a:
    ans[ord(a.pop()) - ord('a')] += 1

print(*ans)