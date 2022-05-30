def solution(genres, plays):
    song = {}
    genre = {}
    answer = []
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in song:
            song[g] = [(i, p)]
        else:
            song[g].append((i, p))

        if g not in genre:
            genre[g] = p
        else:
            genre[g] += p

    for (k, v) in sorted(genre.items(), key=lambda x: x[1], reverse=True):
        cnt = 0
        for (i, p) in sorted(song[k], key=lambda x: x[1], reverse=True):
            if cnt == 2:
                break
            answer.append(i)
            cnt += 1

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 500, 2500]))
