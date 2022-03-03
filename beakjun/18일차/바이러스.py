def make_graph():
    com = {}
    for i in range(int(input())):
        com[i + 1] = set()
    for j in range(int(input())):
        a, b = map(int, input().split())
        com[a].add(b)
        com[b].add(a)
    return com


def solution(start, com):
    visit = []

    queue = [start]
    while queue:
        for i in com[queue.pop(0)]:
            if i not in visit:
                visit.append(i)
                queue.append(i)
    print(len(visit) - 1)


if __name__ == "__main__":
    solution(1, make_graph())
