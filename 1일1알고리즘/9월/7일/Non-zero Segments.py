n = int(input())
a = list(map(int, input().split()))
pref = [0] * 200001
dic = dict()
ans = 0
dic[0] = 1
for i in range(n):
    pref[i] = a[i]
    if i != 0:
        pref[i] += pref[i - 1]
    if pref[i] in dic:
        ans += 1
        dic.clear()
        dic[pref[i - 1]] = 1
    dic[pref[i]] = 1
print(ans)
