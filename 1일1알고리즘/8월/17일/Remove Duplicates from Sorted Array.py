class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 1
        s, e = 0, 1
        while e <= l:
            if nums[s] == nums[e - 1]:
                e += 1
            elif nums[s] != nums[e - 1]:
                nums[s + 1], nums[e - 1] = nums[e - 1], nums[s + 1]
                s += 1
                e += 1
        return s + 1