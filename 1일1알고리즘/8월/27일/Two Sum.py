class Solution:
    def twoSum(self, nums, target):
        h = {}
        for idx, k in enumerate(nums):
            a = target - k
            if a in h:
                return h[a], idx
            h[k] = idx
