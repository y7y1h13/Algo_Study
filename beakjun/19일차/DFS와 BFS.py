from collections import deque


def make_graph(N, M):
    graph = dict()
    for i in range(N):
        graph[i + 1] = set()
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)
    return graph


def dfs(V, graph):
    visited = list()
    q = list()
    q.append(V)
    while q:
        node = q.pop()
        if node not in visited:
            q.extend(sorted(list(graph[node]), reverse=True))
            visited.append(node)
    print(*visited)


def bfs(V, graph):
    visited = list()
    q = deque()
    q.append(V)
    while q:
        node = q.popleft()
        if node not in visited:
            q.extend(sorted(list(graph[node])))
            visited.append(node)
    print(*visited)


if __name__ == "__main__":
    N, M, V = map(int, input().split())
    graph = make_graph(N, M)
    dfs(V, graph)
    bfs(V, graph)
