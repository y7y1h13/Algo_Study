class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            x = int(str(abs(x))[::-1])
        else:
            x = int(str(abs(x))[::-1]) * -1

        return x if -2 ** 31 <= x <= 2 ** 31 - 1 else 0