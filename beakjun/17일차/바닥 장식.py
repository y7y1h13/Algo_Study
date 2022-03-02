def solution(N, M, graph):
    count = 0

    for i in range(N):
        a = ''
        for j in range(M):
            if graph[i][j] == '-':
                if graph[i][j] != a:
                    count += 1
            a = graph[i][j]

    for j in range(M):
        a = ''
        for i in range(N):
            if graph[i][j] == '|':
                if graph[i][j] != a:
                    count += 1
            a = graph[i][j]

    print(count)


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = []
    for _ in range(N):
        graph.append(list(input()))
    solution(N, M, graph)
