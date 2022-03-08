def solution():
    idx = 1
    while True:
        word = list(map(str, input()))
        if '-' in word:
            break
        stack = list()
        cnt = 0
        for i in word:
            if i == '{':
                stack.append(i)
            elif stack:
                stack.pop()
            else:
                cnt += 1
                stack.append('{')

        cnt += len(stack) // 2
        print(f'{idx}. {cnt}')
        idx += 1


if __name__ == "__main__":
    solution()
