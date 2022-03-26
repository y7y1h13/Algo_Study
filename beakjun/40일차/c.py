def solution(arr, brr):
    answer = 0
    for i in range(len(arr) - 1):
        if arr[i] == brr[i]:
            continue
        elif arr[i] < brr[i]:
            n = brr[i] - arr[i]
            arr[i + 1] -= n
            arr[i] += n
            answer += 1
        elif arr[i] > brr[i]:
            n = arr[i] - brr[i]
            arr[i + 1] += n
            arr[i] -= n
            answer += 1
    return answer


print(solution([3, 7, 2, 4], [4, 5, 5, 2]))
