def solution(nums):
    count = len(set(nums))
    max = len(nums) / 2
    if max >= count:
        return count
    elif max < count:
        return max
    return 0