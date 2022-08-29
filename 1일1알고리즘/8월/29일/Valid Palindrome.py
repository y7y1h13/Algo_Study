import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = re.sub(r"[^a-zA-Z]", "", s).lower()
        l, r = 0, len(result) - 1
        while l < len(result) // 2:
            if result[l] == result[r]:
                l += 1
                r -= 1
                continue
            else:
                return False
        return True


a = Solution()
print(a.isPalindrome("race a car"))