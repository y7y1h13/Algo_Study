word = list(map(str, input()))
key = input()
tmp = ''
cnt = 0
for i in word:
    tmp += i
    if key in tmp:
        cnt += 1
        tmp = ''
print(cnt)
