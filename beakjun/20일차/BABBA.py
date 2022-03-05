def solution(K):
    ba = [[] for _ in range(46)]
    ba[0] = [1, 0]
    ba[1] = [0, 1]
    for t in range(2, K + 1):
        ba[t] = [i + j for i, j in zip(ba[t - 1], ba[t - 2])]

    print(ba[K][0], ba[K][1])


if __name__ == "__main__":
    solution(int(input()))
