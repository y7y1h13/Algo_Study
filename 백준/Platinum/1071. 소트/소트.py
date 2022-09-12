from collections import Counter

n = int(input())
a = list(map(int, input().split()))
count = Counter(a)
a_len = n
sort_num = sorted(count)
ans = list()
while a_len > 0:

    for k in range(len(sort_num)):
        flag = True
        i = sort_num[k]
        if count[i] != 0:
            if i + 1 in sort_num and count[i + 1] != 0:
                for j in sort_num[k + 1:]:
                    if i + 2 <= j and count[j] != 0:
                        while count[i]:
                            ans.append(i)
                            count[i] -= 1
                            a_len -= 1
                        ans.append(j)
                        count[j] -= 1
                        a_len -= 1
                        flag = False
                        break
                if flag:
                    ans.append(i + 1)
                    count[i + 1] -= 1
                    a_len -= 1
            else:
                while count[i]:
                    ans.append(i)
                    count[i] -= 1
                    a_len -= 1
print(*ans)
