class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.rev(nums, 0, len(nums) - 1)
        self.rev(nums, 0, k - 1)
        self.rev(nums, k, len(nums) - 1)

    def rev(self, nums, s, e):
        """
        reverse function
        """
        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1

        return nums


a = Solution()
a.rotate([1, 2], 3)