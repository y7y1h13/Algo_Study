import sys

M = int(sys.stdin.readline())
S = set()
for _ in range(M):
    comm = sys.stdin.readline().split()
    if len(comm) == 2:
        x = int(comm[1])
        if comm[0] == "add":
            S.add(x)
        elif comm[0] == "remove":
            S.discard(x)
        elif comm[0] == "toggle":
            S.remove(x) if x in S else S.add(x)
        else:
            print(1 if x in S else 0)
    else:
        if comm[0] == 'all':
            S = set([i for i in range(1, 21)])

        else:
            S.clear()


