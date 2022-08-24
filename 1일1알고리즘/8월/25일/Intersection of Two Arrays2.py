class Solution:
    def intersect(self, nums1, nums2):
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        # a = collections.Counter(nums1)
        a = {}
        for i in nums1:
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1
        ans = []
        for i in nums2:
            if i in a and a[i]:
                ans.append(i)
                a[i] -= 1
                if not a[i]:
                    del a[i]
        return ans


a = Solution()
print(a.intersect([4, 9, 5, 4], [9, 4, 9, 8, 4]))
