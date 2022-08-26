class Solution:
    def plusOne(self, digits):
        # n = (int(''.join(map(str, digits)))) + 1
        # return list(map(int, list(str(n))))
        flag = False
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                flag = True
            else:
                digits[i] += 1
                flag = False
                break
        if flag:
            digits = [1] + digits
        return digits


a = Solution()
print(a.plusOne([8, 9, 9, 9]))
