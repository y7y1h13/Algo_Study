class Solution:
    def singleNumber(self, nums):
        result = 0
        for i in nums:
            result = result^i
        return result
#
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         s = set()
#         for i in nums:
#             if i not in s:
#                 s.add(i)
#             else:
#                 s.remove(i)
#         return list(s)[0]