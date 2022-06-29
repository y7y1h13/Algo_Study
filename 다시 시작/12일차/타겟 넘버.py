class A:
    answer = 0

    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target

    def rec(self, s, cnt):
        if cnt == len(self.numbers):
            if s == self.target:
                self.answer += 1
                return
            else:
                return
        self.rec(s + self.numbers[cnt], cnt + 1)

        self.rec(s - self.numbers[cnt], cnt + 1)

    def solution(self):
        self.rec(0, 0)

        return self.answer


def solution(numbers, target):
    a = A(numbers, target)
    return a.solution()
# answer = 0
#
#
# def rec(s, cnt, numbers, target):
#     global answer
#     if cnt == len(numbers):
#         if s == target:
#             answer += 1
#             return
#         else:
#             return
#     rec(s + numbers[cnt], cnt + 1, numbers, target)
#
#     rec(s - numbers[cnt], cnt + 1, numbers, target)
#
#
# def solution(numbers, target):
#     global answer
#     rec(0, 0, numbers, target)
#
#     return answer
