import sys
input = sys.stdin.readline


def solution():
    q = []
    s, e = 0, 0
    for i in range(int(input())):
        op = input().split()

        if len(op) == 2:
            q.append(int(op[1]))
            e += 1
        else:
            if op[0] == 'pop':
                if s != e:
                    print(q[s])
                    s += 1
                else:
                    print(-1)

            elif op[0] == 'size':
                print(e - s)

            elif op[0] == 'empty':
                if s != e:
                    print(0)
                else:
                    print(1)

            elif op[0] == 'front':
                if s != e:
                    print(q[s])
                else:
                    print(-1)
            else:
                if s != e:
                    print(q[e - 1])
                else:
                    print(-1)


if __name__ == '__main__':
    solution()