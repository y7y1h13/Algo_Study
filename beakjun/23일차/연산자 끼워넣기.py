from itertools import permutations
N = int(input())
num = list(map(int, input().split()))
t = list(map(int, input().split()))
op_lst = ['+', '-', '*', '/']
op = []
m1 = -1e9
m2 = 1e9
for k in range(len(t)):
    for i in range(t[k]):
        op.append(op_lst[k])
oper = list(set(permutations(op,len(op))))

answer = []

answer = []
for i in oper:
    n = num[0]
    for j in range(len(num) - 1):
        if i[j] == '+':
            n += num[j + 1]
        elif i[j] == '-':
            n -= num[j + 1]
        elif i[j] == '*':
            n *= num[j + 1]
        else:
            if n // num[j + 1] < 0:
                n = -(-n // num[j + 1])
            else:
                n = n // num[j + 1]

    answer.append(n)
print(max(answer))
print(min(answer))
