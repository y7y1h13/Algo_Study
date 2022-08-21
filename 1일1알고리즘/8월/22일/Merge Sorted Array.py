class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m + n - 1
        s1 = m - 1
        s2 = n - 1
        while s1 >=0 and s2 >= 0:
            if nums1[s1] > nums2[s2]:
                nums1[l] = nums1[s1]
                s1 -= 1
            else:
                nums1[l] = nums2[s2]
                s2 -= 1
            l -= 1

        if s2 >= 0:
            nums1[:s2 + 1] = nums2[:s2 + 1]


s = Solution()
s.merge([1, 2, 3, 0, 0, 0],
        3,
        [2, 5, 6],
        3)
