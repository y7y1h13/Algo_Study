class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        if l > 1:
            f = 0
            e = l - 1
            while f < e:
                s[f], s[e] = s[e], s[f]
                f += 1
                e -= 1