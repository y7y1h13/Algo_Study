class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s, e = 0, 1
        while e < len(nums):
            if nums[s] == 0 and nums[e] == 0:
                e += 1
            elif nums[s] == 0 and nums[e] != 0:
                nums[s], nums[e] = nums[e], nums[s]
                s += 1
                e += 1
            else:
                s += 1
                e += 1